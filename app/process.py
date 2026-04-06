"""对话处理接口 - 集成 DashScope API"""

import json
import uuid
from typing import AsyncGenerator
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from .models import ProcessRequest, ProcessResponse, Message, ContentItem, StreamChunk
from .config import config

# 尝试导入 agentscope-runtime 用于可观测性
try:
    from agentscope.runtime import trace
    AGENTSCOPE_AVAILABLE = True
except ImportError:
    AGENTSCOPE_AVAILABLE = False
    trace = None

# 导入 DashScope
try:
    import dashscope
    from dashscope import Generation
    DASHSCOPE_AVAILABLE = True
except ImportError:
    DASHSCOPE_AVAILABLE = False
    dashscope = None

router = APIRouter()


def convert_to_dashscope_messages(messages: list[Message]) -> list[dict]:
    """
    将内部消息格式转换为 DashScope API 格式
    
    Args:
        messages: 内部 Message 对象列表
        
    Returns:
        list[dict]: DashScope 格式的消息列表
    """
    dashscope_messages = []
    for msg in messages:
        content = msg.get_text_content()
        dashscope_messages.append({
            "role": msg.role,
            "content": content
        })
    return dashscope_messages


async def stream_response(
    session_id: str,
    user_input: str
) -> AsyncGenerator[str, None]:
    """
    流式响应生成器
    
    Args:
        session_id: 会话 ID
        user_input: 用户输入文本
        
    Yields:
        str: SSE 格式的数据块
    """
    request_id = str(uuid.uuid4())
    
    # 配置 DashScope
    if dashscope:
        dashscope.api_key = config.DASHSCOPE_API_KEY
    
    try:
        # 使用 agentscope-runtime 追踪（如果可用）
        if AGENTSCOPE_AVAILABLE and trace:
            with trace(
                name="process_request",
                tags={"session_id": session_id, "user_id": "user"}
            ):
                response = Generation.call(
                    model=config.MODEL_NAME,
                    messages=[{"role": "user", "content": user_input}],
                    stream=True,
                    result_format="message"
                )
        else:
            response = Generation.call(
                model=config.MODEL_NAME,
                messages=[{"role": "user", "content": user_input}],
                stream=True,
                result_format="message"
            )
        
        # 处理流式响应
        full_content = ""
        for chunk in response:
            if chunk.status_code == 200:
                content = chunk.output.choices[0].message.content
                delta = content[len(full_content):]
                full_content = content
                
                stream_chunk = StreamChunk(
                    content=delta,
                    role="assistant"
                )
                yield f"data: {stream_chunk.model_dump_json()}\n\n"
            else:
                error_chunk = {
                    "error": f"API Error: {chunk.code} - {chunk.message}"
                }
                yield f"data: {json.dumps(error_chunk)}\n\n"
        
        # 发送结束标记
        yield "data: [DONE]\n\n"
        
    except Exception as e:
        error_chunk = {"error": str(e)}
        yield f"data: {json.dumps(error_chunk)}\n\n"
        yield "data: [DONE]\n\n"


@router.post("/process")
async def process(request: ProcessRequest):
    """
    对话处理接口
    
    Args:
        request: ProcessRequest 对象，包含 input, session_id, user_id
        
    Returns:
        ProcessResponse 或 StreamingResponse: 对话响应
        
    请求格式:
        {
            "input": [{"role": "user", "content": [{"type": "text", "text": "你好"}]}],
            "session_id": "test-session",
            "user_id": "test-user",
            "stream": false
        }
    """
    # 验证配置
    config.validate()
    
    # 获取用户输入
    user_input = request.get_last_user_message()
    if not user_input:
        raise HTTPException(status_code=400, detail="无效的用户输入")
    
    # 检查 DashScope 可用性
    if not DASHSCOPE_AVAILABLE:
        raise HTTPException(status_code=503, detail="DashScope SDK 未安装")
    
    # 配置 API Key
    dashscope.api_key = config.DASHSCOPE_API_KEY
    
    try:
        # 转换为 DashScope 消息格式
        messages = convert_to_dashscope_messages(request.input)
        
        # 使用 agentscope-runtime 追踪（如果可用）
        if AGENTSCOPE_AVAILABLE and trace:
            with trace(
                name="process_request",
                tags={
                    "session_id": request.session_id,
                    "user_id": request.user_id
                }
            ):
                response = Generation.call(
                    model=config.MODEL_NAME,
                    messages=messages,
                    stream=request.stream,
                    result_format="message"
                )
        else:
            response = Generation.call(
                model=config.MODEL_NAME,
                messages=messages,
                stream=request.stream,
                result_format="message"
            )
        
        # 处理响应
        if request.stream:
            # 流式响应
            return StreamingResponse(
                stream_response(request.session_id, user_input),
                media_type="text/event-stream"
            )
        else:
            # 非流式响应
            if response.status_code == 200:
                assistant_message = Message(
                    role="assistant",
                    content=[ContentItem(type="text", text=response.output.choices[0].message.content)]
                )
                
                return ProcessResponse(
                    output=[assistant_message],
                    session_id=request.session_id,
                    usage=response.usage if hasattr(response, 'usage') else None,
                    request_id=response.request_id if hasattr(response, 'request_id') else None
                )
            else:
                raise HTTPException(
                    status_code=500,
                    detail=f"DashScope API 错误：{response.code} - {response.message}"
                )
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"处理请求失败：{str(e)}")

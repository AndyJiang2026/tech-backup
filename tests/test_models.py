"""数据模型测试"""

import pytest
from app.models import (
    ContentItem,
    Message,
    ProcessRequest,
    ProcessResponse,
    StreamChunk,
    HealthResponse
)


def test_content_item():
    """测试内容项模型"""
    item = ContentItem(type="text", text="测试内容")
    assert item.type == "text"
    assert item.text == "测试内容"


def test_message():
    """测试消息模型"""
    msg = Message(
        role="user",
        content=[
            ContentItem(type="text", text="你好"),
            ContentItem(type="text", text="世界")
        ]
    )
    assert msg.role == "user"
    assert msg.get_text_content() == "你好\n世界"


def test_process_request():
    """测试处理请求模型"""
    request = ProcessRequest(
        input=[
            Message(
                role="user",
                content=[ContentItem(type="text", text="你好")]
            )
        ],
        session_id="test-session",
        user_id="test-user"
    )
    
    assert request.session_id == "test-session"
    assert request.user_id == "test-user"
    assert request.get_last_user_message() == "你好"


def test_process_response():
    """测试处理响应模型"""
    response = ProcessResponse(
        output=[
            Message(
                role="assistant",
                content=[ContentItem(type="text", text="你好！")]
            )
        ],
        session_id="test-session"
    )
    
    assert len(response.output) == 1
    assert response.output[0].role == "assistant"


def test_stream_chunk():
    """测试流式块模型"""
    chunk = StreamChunk(
        content="测试",
        role="assistant"
    )
    
    assert chunk.content == "测试"
    assert chunk.role == "assistant"
    assert chunk.finish_reason is None


def test_health_response():
    """测试健康响应模型"""
    response = HealthResponse()
    
    assert response.status == "OK"
    assert response.version == "1.0.0"
    assert response.app_name == "openclaw-team"

"""数据模型定义"""

from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class ContentItem(BaseModel):
    """消息内容项"""
    
    type: Literal["text", "image", "file"] = "text"
    text: Optional[str] = None
    image_url: Optional[str] = None
    file_url: Optional[str] = None


class Message(BaseModel):
    """对话消息"""
    
    role: Literal["user", "assistant", "system"] = "user"
    content: List[ContentItem] = Field(default_factory=list)
    
    def get_text_content(self) -> str:
        """获取纯文本内容"""
        texts = []
        for item in self.content:
            if item.type == "text" and item.text:
                texts.append(item.text)
        return "\n".join(texts)


class ProcessRequest(BaseModel):
    """处理请求模型"""
    
    input: List[Message] = Field(..., description="对话历史")
    session_id: str = Field(..., description="会话 ID")
    user_id: str = Field(..., description="用户 ID")
    stream: bool = Field(default=False, description="是否流式响应")
    
    def get_last_user_message(self) -> Optional[str]:
        """获取最后一条用户消息"""
        for msg in reversed(self.input):
            if msg.role == "user":
                return msg.get_text_content()
        return None


class ProcessResponse(BaseModel):
    """处理响应模型"""
    
    output: List[Message] = Field(default_factory=list)
    session_id: str
    usage: Optional[dict] = None
    request_id: Optional[str] = None


class StreamChunk(BaseModel):
    """流式响应块"""
    
    content: str
    role: str = "assistant"
    finish_reason: Optional[str] = None
    usage: Optional[dict] = None


class HealthResponse(BaseModel):
    """健康检查响应"""
    
    status: str = "OK"
    version: str = "1.0.0"
    app_name: str = "openclaw-team"

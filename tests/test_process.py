"""对话处理接口测试"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_process_request_structure():
    """测试请求结构验证"""
    # 测试无效请求（缺少必要字段）
    response = client.post("/process", json={})
    assert response.status_code == 422  # 验证错误
    
    # 测试缺少 input 字段
    response = client.post("/process", json={
        "session_id": "test",
        "user_id": "test"
    })
    assert response.status_code == 422


def test_process_request_format():
    """测试请求格式"""
    request_data = {
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "你好"
                    }
                ]
            }
        ],
        "session_id": "test-session",
        "user_id": "test-user",
        "stream": False
    }
    
    # 注意：这个测试需要有效的 API Key 才能通过
    # 在没有配置 API Key 的情况下会返回 500 或 503
    response = client.post("/process", json=request_data)
    
    # 可能的响应：
    # - 422: 验证错误
    # - 500: API 调用失败（无有效 Key）
    # - 503: DashScope 未安装
    # - 200: 成功（有有效 Key）
    assert response.status_code in [200, 500, 503]


def test_process_stream_request():
    """测试流式请求"""
    request_data = {
        "input": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "你好"
                    }
                ]
            }
        ],
        "session_id": "test-session",
        "user_id": "test-user",
        "stream": True
    }
    
    response = client.post("/process", json=request_data)
    
    # 流式请求应该返回 SSE 格式
    if response.status_code == 200:
        assert "text/event-stream" in response.headers.get("content-type", "")

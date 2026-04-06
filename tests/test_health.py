"""健康检查接口测试"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    """测试健康检查接口"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.text == "OK"


def test_health_check_detail():
    """测试详细健康检查接口"""
    response = client.get("/health/detail")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "OK"
    assert data["version"] == "1.0.0"
    assert data["app_name"] == "openclaw-team"


def test_root_endpoint():
    """测试根路径"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "openclaw-team"
    assert data["version"] == "1.0.0"
    assert data["status"] == "running"

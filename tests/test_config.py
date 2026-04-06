"""配置管理测试"""

import pytest
import os
from app.config import Config, config


def test_config_defaults():
    """测试默认配置"""
    assert config.APP_NAME == "openclaw-team"
    assert config.DEPLOY_REGION == "cn-beijing"
    assert config.HOST == "0.0.0.0"
    assert config.PORT == 8000
    assert config.DEBUG is False


def test_config_validate():
    """测试配置验证"""
    # 默认应该有 API Key
    assert config.validate() is True


def test_config_alibaba_credentials():
    """测试阿里云凭证获取"""
    creds = config.get_alibaba_credentials()
    assert isinstance(creds, dict)
    assert "access_key_id" in creds
    assert "access_key_secret" in creds
    assert "workspace_id" in creds


def test_config_from_env():
    """测试从环境变量读取配置"""
    # 保存原值
    original_key = os.getenv("DASHSCOPE_API_KEY")
    
    try:
        # 设置测试值
        os.environ["DASHSCOPE_API_KEY"] = "test-key-123"
        os.environ["MODEL_NAME"] = "dashscope/test-model"
        
        # 重新创建配置实例
        test_config = Config()
        
        assert test_config.DASHSCOPE_API_KEY == "test-key-123"
        assert test_config.MODEL_NAME == "dashscope/test-model"
    finally:
        # 恢复原值
        if original_key:
            os.environ["DASHSCOPE_API_KEY"] = original_key
        else:
            os.environ.pop("DASHSCOPE_API_KEY", None)

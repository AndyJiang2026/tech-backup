"""配置管理模块"""

import os
from typing import Optional


class Config:
    """应用配置"""

    # 阿里云百炼配置
    DASHSCOPE_API_KEY: str = os.getenv(
        "DASHSCOPE_API_KEY",
        "sk-a6e9b4cd251d467eaaa76d0e7a82405f"
    )
    
    # 模型配置
    MODEL_NAME: str = os.getenv("MODEL_NAME", "dashscope/qwen-coder-plus")
    
    # 应用配置
    APP_NAME: str = os.getenv("APP_NAME", "openclaw-team")
    DEPLOY_REGION: str = os.getenv("DEPLOY_REGION", "cn-beijing")
    
    # 阿里云凭证（用于部署）
    ALIBABA_CLOUD_ACCESS_KEY_ID: Optional[str] = os.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID")
    ALIBABA_CLOUD_ACCESS_KEY_SECRET: Optional[str] = os.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
    MODELSTUDIO_WORKSPACE_ID: Optional[str] = os.getenv("MODELSTUDIO_WORKSPACE_ID")
    
    # 服务配置
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    @classmethod
    def validate(cls) -> bool:
        """验证必要配置是否存在"""
        if not cls.DASHSCOPE_API_KEY:
            raise ValueError("DASHSCOPE_API_KEY 未配置")
        return True
    
    @classmethod
    def get_alibaba_credentials(cls) -> dict:
        """获取阿里云凭证"""
        return {
            "access_key_id": cls.ALIBABA_CLOUD_ACCESS_KEY_ID,
            "access_key_secret": cls.ALIBABA_CLOUD_ACCESS_KEY_SECRET,
            "workspace_id": cls.MODELSTUDIO_WORKSPACE_ID,
        }


# 全局配置实例
config = Config()

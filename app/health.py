"""健康检查接口"""

from fastapi import APIRouter
from .models import HealthResponse
from .config import config

router = APIRouter()


@router.get("/health")
async def health_check() -> str:
    """
    健康检查接口
    
    返回:
        str: "OK" 表示服务正常
    """
    return "OK"


@router.get("/health/detail", response_model=HealthResponse)
async def health_check_detail() -> HealthResponse:
    """
    详细健康检查接口
    
    返回:
        HealthResponse: 包含服务状态、版本等信息
    """
    return HealthResponse(
        status="OK",
        version="1.0.0",
        app_name=config.APP_NAME
    )

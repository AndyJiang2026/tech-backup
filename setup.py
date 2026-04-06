"""
OpenClaw Team - 打包配置
"""

from setuptools import setup, find_packages

setup(
    name="openclaw-team",
    version="1.0.0",
    description="OpenClaw Team - 阿里云百炼高代码应用",
    author="OpenClaw Team",
    author_email="team@openclaw.com",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "fastapi==0.109.0",
        "uvicorn==0.27.0",
        "dashscope==1.14.1",
        "agentscope-runtime==1.0.0",
        "pydantic==2.5.0",
    ],
    extras_require={
        "deployment": [
            "agentscope-runtime[deployment]==1.0.0",
        ],
        "dev": [
            "pytest==7.4.0",
            "pytest-asyncio==0.21.0",
            "httpx==0.25.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "openclaw-team=main:app",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

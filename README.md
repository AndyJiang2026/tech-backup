# OpenClaw Team - 阿里云百炼高代码应用

OpenClaw 团队的阿里云百炼高代码应用，基于 FastAPI 和 DashScope API 构建。

## 📁 项目结构

```
bailian-app/
├── main.py                 # FastAPI 入口文件
├── app/
│   ├── __init__.py         # 包初始化
│   ├── health.py           # 健康检查接口
│   ├── process.py          # 对话处理接口
│   ├── config.py           # 配置管理
│   └── models.py           # 数据模型
├── requirements.txt        # 依赖清单
├── setup.py               # 打包配置
└── README.md              # 部署说明
```

## 🚀 快速开始

### 1. 环境要求

- Python >= 3.10
- 阿里云账号（用于百炼平台）

### 2. 安装依赖

```bash
# 基础依赖
pip install -r requirements.txt

# 或者使用 agentscope-runtime 部署版本
pip install agentscope-runtime==1.0.0
pip install "agentscope-runtime[deployment]==1.0.0"
```

### 3. 配置环境变量

```bash
# DashScope API Key（必填）
export DASHSCOPE_API_KEY=sk-a6e9b4cd251d467eaaa76d0e7a82405f

# 可选配置
export MODEL_NAME=dashscope/qwen-coder-plus
export APP_NAME=openclaw-team
export DEPLOY_REGION=cn-beijing
export HOST=0.0.0.0
export PORT=8000
export DEBUG=false

# 阿里云凭证（部署时需要）
export ALIBABA_CLOUD_ACCESS_KEY_ID=LTAI************
export ALIBABA_CLOUD_ACCESS_KEY_SECRET=****************
export MODELSTUDIO_WORKSPACE_ID=llm-****************
```

### 4. 本地运行

```bash
# 方式 1: 直接运行
python main.py

# 方式 2: 使用 uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# 方式 3: 开发模式
DEBUG=true python main.py
```

### 5. 测试接口

#### 健康检查

```bash
curl http://localhost:8000/health
# 返回：OK
```

#### 对话接口

```bash
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "你好，请介绍一下自己"
          }
        ]
      }
    ],
    "session_id": "test-session-001",
    "user_id": "test-user-001",
    "stream": false
  }'
```

#### 流式对话

```bash
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{
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
    "session_id": "test-session-001",
    "user_id": "test-user-001",
    "stream": true
  }'
```

## 📦 打包部署

### 1. 打包

```bash
python setup.py bdist_wheel
```

生成的 wheel 文件位于 `dist/` 目录。

### 2. 部署到阿里云百炼

```bash
# 使用 runtime-fc-deploy 命令
runtime-fc-deploy \
  --deploy-name openclaw-team \
  --whl-path dist/*.whl \
  --telemetry enable
```

### 3. 验证部署

部署完成后，访问百炼平台提供的 endpoint 进行测试：

```bash
curl https://<your-endpoint>/health
```

## 🔌 API 接口文档

### GET /health

健康检查接口

**响应示例:**
```
OK
```

### GET /health/detail

详细健康检查

**响应示例:**
```json
{
  "status": "OK",
  "version": "1.0.0",
  "app_name": "openclaw-team"
}
```

### POST /process

对话处理接口

**请求体:**
```json
{
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
  "session_id": "session-123",
  "user_id": "user-456",
  "stream": false
}
```

**响应体（非流式）:**
```json
{
  "output": [
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "你好！我是 OpenClaw 助手..."
        }
      ]
    }
  ],
  "session_id": "session-123",
  "usage": {
    "input_tokens": 10,
    "output_tokens": 50
  },
  "request_id": "req-xxx"
}
```

**流式响应（SSE 格式）:**
```
data: {"content":"你","role":"assistant"}

data: {"content":"好","role":"assistant"}

data: [DONE]
```

## 📊 可观测性

本应用集成了 AgentScope-runtime，支持：

- 请求追踪（Trace）
- 性能监控
- 错误日志

启用方式：部署时添加 `--telemetry enable` 参数。

## 🛠️ 开发

### 安装开发依赖

```bash
pip install -e ".[dev]"
```

### 运行测试

```bash
pytest tests/ -v
```

## ⚠️ 注意事项

1. **API Key 安全**: 不要将 API Key 提交到代码仓库
2. **环境变量**: 生产环境请使用环境变量管理敏感信息
3. **速率限制**: DashScope API 有调用频率限制，请注意控制请求频率
4. **错误处理**: 生产环境建议添加重试机制和熔断器

## 📝 版本历史

- v1.0.0 (2026-03-29): 初始版本
  - 实现 /health 健康检查接口
  - 实现 /process 对话处理接口
  - 集成 DashScope API (qwen-coder-plus)
  - 支持流式和非流式响应
  - 集成 AgentScope-runtime 可观测性

## 🤝 联系方式

- 团队：OpenClaw Team
- 应用名称：openclaw-team
- 部署区域：cn-beijing

---

**开始构建你的 AI 应用吧！** 🚀

# 备用模型配置方案

**日期**: 2026-04-17 18:40 GMT+8  
**目标**: 配置多模型备份，提高系统可靠性

---

## 📊 当前模型配置

### chief-agent（强国小马）

**已配置提供商**（3 个）:

| 提供商 | 模型 | 状态 | 用途 |
|--------|------|------|------|
| dashscope-coding | qwen3-max-2026-01-23 | ✅ | 代码生成 |
| dashscope-coding | qwen3.5-plus | ✅ | 通用对话 |
| dashscope | qwen3.5-plus | ✅ | 通用对话（备用） |
| dashscope-image | wanx-v1 | ✅ | 图像生成 |

### main-agent

**已配置提供商**（2 个）:

| 提供商 | 模型 | 状态 |
|--------|------|------|
| minimax | abab6.5-chat | ✅ |
| dashscope | qwen3.5-plus | ✅ |

---

## 🎯 备用模型方案

### 方案 A：同提供商多模型备份 ⭐⭐⭐

**配置多个通义千问模型**:
```json
{
  "dashscope": {
    "models": [
      {"id": "qwen3.5-plus", "priority": 1},
      {"id": "qwen3-max-2026-01-23", "priority": 2},
      {"id": "qwen-plus", "priority": 3}
    ]
  }
}
```

**优势**:
- ✅ 配置简单
- ✅ 切换快速
- ✅ API 兼容性好

**劣势**:
- ⚠️ 单提供商风险（阿里云故障时全部不可用）

---

### 方案 B：多提供商备份 ⭐⭐⭐⭐

**配置多个不同提供商**:
```json
{
  "providers": {
    "dashscope": {
      "models": ["qwen3.5-plus"]
    },
    "minimax": {
      "models": ["abab6.5-chat"]
    },
    "zhipu": {
      "models": ["glm-4"]
    }
  }
}
```

**优势**:
- ✅ 多提供商容灾
- ✅ 不同模型特点互补
- ✅ 成本优化空间大

**劣势**:
- ⚠️ 配置复杂
- ⚠️ 需要多个 API Key

---

### 方案 C：智能路由备份 ⭐⭐⭐⭐⭐

**根据场景自动选择模型**:
```
简单问题 → qwen-plus（快速/便宜）
复杂分析 → qwen3.5-plus（平衡）
深度推理 → qwen3-max（最强）
代码生成 → qwen3-max-2026-01-23（代码优化）
图像生成 → wanx-v1
```

**优势**:
- ✅ 成本最优
- ✅ 性能最优
- ✅ 自动容灾

**劣势**:
- ⚠️ 需要路由逻辑
- ⚠️ 配置复杂

---

## 🔧 推荐配置（方案 B+C 组合）

### 第一梯队：主力模型
- **qwen3.5-plus**（通义）- 日常对话/分析
- **qwen3-max-2026-01-23**（通义）- 复杂任务/代码

### 第二梯队：备用模型
- **abab6.5-chat**（MiniMax）- 对话备用
- **glm-4**（智谱）- 分析备用

### 第三梯队：经济模型
- **qwen-plus**（通义）- 简单任务
- **abab6.5-turbo**（MiniMax）- 快速响应

---

## 📁 配置步骤

### 步骤 1：获取 API Key
```bash
# 通义千问（已有）
sk-a6e9b4cd251d467eaaa76d0e7a82405f

# MiniMax（已有）
sk-api-SWx6QpGZbDtU2...

# 智谱 AI（需获取）
https://open.bigmodel.cn/
```

### 步骤 2：更新 models.json
```json
{
  "providers": {
    "dashscope": {
      "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
      "apiKey": "sk-a6e9b4cd251d467eaaa76d0e7a82405f",
      "models": [
        {"id": "qwen3.5-plus", "priority": 1},
        {"id": "qwen3-max-2026-01-23", "priority": 2},
        {"id": "qwen-plus", "priority": 3}
      ]
    },
    "minimax": {
      "baseUrl": "https://api.minimax.io/anthropic",
      "apiKey": "sk-api-...",
      "models": [
        {"id": "abab6.5-chat", "priority": 1},
        {"id": "abab6.5-turbo", "priority": 2}
      ]
    }
  }
}
```

### 步骤 3：配置故障转移
```json
{
  "failover": {
    "enabled": true,
    "timeout": 30000,
    "retries": 3,
    "fallback_order": ["dashscope", "minimax", "zhipu"]
  }
}
```

---

## 📊 模型对比

| 模型 | 提供商 | 上下文 | 速度 | 成本 | 适用场景 |
|------|--------|--------|------|------|---------|
| qwen3.5-plus | 通义 | 1M | 快 | 中 | 通用对话 |
| qwen3-max | 通义 | 256K | 中 | 高 | 复杂任务 |
| qwen-plus | 通义 | 128K | 快 | 低 | 简单任务 |
| abab6.5-chat | MiniMax | 200K | 快 | 中 | 对话备用 |
| glm-4 | 智谱 | 128K | 中 | 中 | 分析备用 |

---

## 🎯 推荐方案

### 立即配置（今天内）
1. ✅ 添加 qwen3-max-2026-01-23 为主力
2. ✅ 添加 qwen-plus 为经济选项
3. ✅ 配置故障转移逻辑

### 本周内配置
1. ⚪ 获取智谱 AI API Key
2. ⚪ 添加 glm-4 为备用
3. ⚪ 测试多模型切换

### 本月内优化
1. ⚪ 智能路由逻辑
2. ⚪ 成本监控
3. ⚪ 性能分析

---

## 💡 使用示例

### 示例 1：简单问题（经济模式）
```
用户："今天天气如何？"
→ 自动选择 qwen-plus
→ 快速响应
→ 成本最低
```

### 示例 2：复杂分析（主力模式）
```
用户："分析一下这个商业计划"
→ 自动选择 qwen3.5-plus
→ 深度分析
→ 成本适中
```

### 示例 3：代码生成（专业模式）
```
用户："帮我写个 Python 脚本"
→ 自动选择 qwen3-max-2026-01-23
→ 代码优化
→ 质量优先
```

### 示例 4：主力模型故障
```
用户："分析一下这个问题"
→ qwen3.5-plus 超时
→ 自动切换到 abab6.5-chat
→ 继续响应
→ 用户无感知
```

---

## ✅ 执行清单

### 今天内
- [ ] 更新 models.json（添加 qwen3-max/qwen-plus）
- [ ] 配置故障转移逻辑
- [ ] 测试模型切换

### 本周内
- [ ] 获取智谱 AI API Key
- [ ] 添加 glm-4 模型
- [ ] 完整测试

### 本月内
- [ ] 智能路由逻辑
- [ ] 成本监控面板
- [ ] 性能分析报告

---

**制定者**: 强国小马（chief-agent）  
**日期**: 2026-04-17 18:40 GMT+8  
**状态**: 🟡 方案完成，待执行

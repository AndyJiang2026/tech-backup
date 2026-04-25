# 所有 Agent 模型配置全面回顾

**回顾时间**: 2026-04-18 01:40 GMT+8  
**状态**: ✅ 配置完整

---

## 🤖 Agent 团队架构

```
┌─────────────────────────┐
│   强国小马 (chief-agent) │  主模型：DeepSeek Reasoner
│   Leader / 任务分发      │  备用：qwen3.5-plus
└──────────┬──────────────┘
           │
    ┌──────┴──────┐
    │             │
    ▼             ▼
┌────────┐  ┌────────────┐
│ main   │  │ 专业 Agent  │
│ agent  │  │ (5 个)      │
└────────┘  └────────────┘
主模型：     共用 chief-agent
DeepSeek    技能配置
Reasoner
```

---

## 📊 模型配置详情

### 1️⃣ chief-agent（强国小马）

**角色**: Team Leader / 任务分发 / 结果汇总

**模型配置**:
| 提供商 | 模型 | 优先级 | 上下文 | 成本 | 用途 |
|--------|------|--------|--------|------|------|
| **deepseek** | **deepseek-reasoner** | **1（主）** | 64K | ¥0.004/千 | 深度推理 |
| **dashscope** | **qwen3.5-plus** | **2（备用）** | 1M | ¥0.004/千 | 通用对话 |

**API Key**:
- DeepSeek: `sk-bf48a6d1a23748e29374b0dab49dfed2` ✅
- DashScope: `sk-a6e9b4cd251d467eaaa76d0e7a82405f` ✅

**智能路由**:
- 默认：deepseek-reasoner
- 分析/推理/逻辑 → deepseek-reasoner
- 图片/设计/海报 → qwen3.5-plus
- 简单/快速/天气 → qwen3.5-plus

**故障转移**:
```
deepseek-reasoner → qwen3.5-plus
```

---

### 2️⃣ main-agent

**角色**: 主要执行 Agent / 备用 Leader

**模型配置**:
| 提供商 | 模型 | 优先级 | 上下文 | 成本 | 用途 |
|--------|------|--------|--------|------|------|
| **deepseek** | **deepseek-reasoner** | **1（主）** | 64K | ¥0.004/千 | 深度推理 |
| **dashscope** | **qwen3.5-plus** | **2（备用）** | 1M | ¥0.004/千 | 通用对话 |

**API Key**:
- DeepSeek: `sk-bf48a6d1a23748e29374b0dab49dfed2` ✅
- DashScope: `sk-a6e9b4cd251d467eaaa76d0e7a82405f` ✅

**故障转移**:
```
deepseek-reasoner → qwen3.5-plus
```

---

### 3️⃣ 专业 Agent（5 个）

**专业 Agent 不独立配置模型**，共用 chief-agent 的模型配置：

| Agent | 角色 | 模型来源 |
|-------|------|---------|
| 运营管理 | 业务流程/数据分析 | chief-agent |
| 财务顾问 | 财务分析/预算管理 | chief-agent |
| 法务顾问 | 合同审查/法律咨询 | chief-agent |
| 文案撰稿 | 营销文案/内容策划 | chief-agent |
| 平面设计 | 视觉设计/图片生成 | chief-agent |

---

## 📈 配置统计

### 总体统计

| 指标 | 数值 |
|------|------|
| Agent 总数 | 7 个（2 个核心 + 5 个专业） |
| 配置模型数 | 2 个（deepseek-reasoner + qwen3.5-plus） |
| 提供商数 | 2 个（deepseek + dashscope） |
| API Key 数 | 2 个（DeepSeek + DashScope） |

### 模型分布

| Agent | 主模型 | 备用模型 | 状态 |
|-------|--------|---------|------|
| chief-agent | deepseek-reasoner | qwen3.5-plus | ✅ |
| main-agent | deepseek-reasoner | qwen3.5-plus | ✅ |
| 运营管理 | deepseek-reasoner | qwen3.5-plus | ✅ |
| 财务顾问 | deepseek-reasoner | qwen3.5-plus | ✅ |
| 法务顾问 | deepseek-reasoner | qwen3.5-plus | ✅ |
| 文案撰稿 | deepseek-reasoner | qwen3.5-plus | ✅ |
| 平面设计 | deepseek-reasoner | qwen3.5-plus | ✅ |

---

## 🔧 模型能力对比

### DeepSeek Reasoner（主模型）

**优势**:
- ✅ 深度推理能力强
- ✅ 逻辑分析优秀
- ✅ 复杂问题处理
- ✅ 数学/代码/科学推理

**限制**:
- ❌ 仅支持文本输入
- ❌ 上下文 64K（相对较小）
- ❌ 不支持图像生成

**适用场景**:
- ✅ 复杂分析任务
- ✅ 逻辑推理问题
- ✅ 代码分析/调试
- ✅ 深度研究报告

---

### Qwen3.5-Plus（备用模型）

**优势**:
- ✅ 多模态支持（text+image）
- ✅ 超大上下文（1M tokens）
- ✅ 通用对话能力强
- ✅ 快速响应

**限制**:
- ❌ 推理能力相对较弱
- ❌ 成本略高（但相同）

**适用场景**:
- ✅ 图像理解任务
- ✅ 长文档分析
- ✅ 通用对话
- ✅ 快速问答
- ✅ 图像生成（wanx-v1）

---

## 🎯 智能路由规则

### chief-agent 路由配置

| 触发词 | 使用模型 | 提供商 | 说明 |
|--------|---------|--------|------|
| "分析"/"推理"/"逻辑" | deepseek-reasoner | deepseek | 深度推理 |
| "复杂"/"深度" | deepseek-reasoner | deepseek | 复杂问题 |
| "代码"/"编程"/"debug" | deepseek-reasoner | deepseek | 代码分析 |
| "图片"/"设计"/"海报" | qwen3.5-plus | dashscope | 多模态 |
| "简单"/"快速"/"天气" | qwen3.5-plus | dashscope | 快速响应 |
| 默认 | deepseek-reasoner | deepseek | 主模型 |

---

## 🛡️ 故障转移配置

### chief-agent

```
deepseek-reasoner（主）
  ↓ [timeout 30s / error 5xx / rate_limit]
qwen3.5-plus（备用）
  ↓ [继续失败]
返回错误（用户可见）
```

**重试策略**:
- 超时：30 秒后切换
- 错误：5xx 立即切换
- 限流：重试 3 次后切换

---

### main-agent

```
deepseek-reasoner（主）
  ↓ [timeout 30s / error 5xx / rate_limit]
qwen3.5-plus（备用）
```

**重试策略**: 同 chief-agent

---

## 💰 成本分析

### 模型成本对比

| 模型 | 输入成本 | 输出成本 | 上下文 |
|------|---------|---------|--------|
| deepseek-reasoner | ¥0.004/千 | ¥0.012/千 | 64K |
| qwen3.5-plus | ¥0.004/千 | ¥0.012/千 | 1M |

**成本相同**，但 deepseek-reasoner 推理能力更强！

---

### 日均成本预估

**假设日均请求**: 100 次

| 模型 | 使用比例 | 日均请求 | 单次成本 | 日均成本 |
|------|---------|---------|---------|---------|
| deepseek-reasoner | 80% | 80 次 | ¥0.004 | ¥0.32 |
| qwen3.5-plus | 20% | 20 次 | ¥0.004 | ¥0.08 |

**日均总成本**: ¥0.40  
**月均总成本**: ¥12.0

---

## 📋 配置验证清单

### chief-agent
- [x] ✅ DeepSeek API Key 已配置
- [x] ✅ DashScope API Key 已配置
- [x] ✅ deepseek-reasoner 为主模型
- [x] ✅ qwen3.5-plus 为备用模型
- [x] ✅ 故障转移配置完整
- [x] ✅ 智能路由配置完整

### main-agent
- [x] ✅ DeepSeek API Key 已配置
- [x] ✅ DashScope API Key 已配置
- [x] ✅ deepseek-reasoner 为主模型
- [x] ✅ qwen3.5-plus 为备用模型
- [x] ✅ 故障转移配置完整

### 专业 Agent
- [x] ✅ 共用 chief-agent 模型配置
- [x] ✅ 技能配置完整（38 个）
- [x] ✅ 场景映射完整（7 个）

---

## 📁 配置文件

| 文件 | 路径 | 状态 |
|------|------|------|
| chief-agent models.json | `/home/admin/.openclaw/agents/chief-agent/agent/models.json` | ✅ |
| main-agent models.json | `/home/admin/.openclaw/agents/main/agent/models.json` | ✅ |
| 配置回顾报告 | `reports/ALL-AGENTS-MODEL-REVIEW-20260418.md` | ✅ |

---

## ✅ 总结

### 模型配置状态

| Agent | 主模型 | 备用模型 | API Key | 状态 |
|-------|--------|---------|--------|------|
| chief-agent | deepseek-reasoner | qwen3.5-plus | ✅ | ✅ 就绪 |
| main-agent | deepseek-reasoner | qwen3.5-plus | ✅ | ✅ 就绪 |
| 运营管理 | deepseek-reasoner | qwen3.5-plus | ✅ | ✅ 就绪 |
| 财务顾问 | deepseek-reasoner | qwen3.5-plus | ✅ | ✅ 就绪 |
| 法务顾问 | deepseek-reasoner | qwen3.5-plus | ✅ | ✅ 就绪 |
| 文案撰稿 | deepseek-reasoner | qwen3.5-plus | ✅ | ✅ 就绪 |
| 平面设计 | deepseek-reasoner | qwen3.5-plus | ✅ | ✅ 就绪 |

### 核心特点

1. ✅ **统一模型配置** - 所有 Agent 使用相同模型
2. ✅ **深度推理优先** - deepseek-reasoner 为主模型
3. ✅ **多模态备用** - qwen3.5-plus 支持图像
4. ✅ **故障转移完整** - 自动切换备用模型
5. ✅ **智能路由** - 按需选择最优模型
6. ✅ **成本可控** - 月均¥12.0

### 可以承接的任务

- ✅ 深度推理分析
- ✅ 复杂逻辑问题
- ✅ 代码分析/调试
- ✅ 多模态任务
- ✅ 长文档分析
- ✅ 图像生成

---

**回顾者**: 强国小马（chief-agent）  
**回顾时间**: 2026-04-18 01:40 GMT+8  
**状态**: ✅ 配置完整，全部就绪

🎉 **所有 Agent 模型配置完整，7 个 Agent 全部就绪，可以承接高复杂度任务！**

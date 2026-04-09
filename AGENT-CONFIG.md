# 🐴 强国小马 Agent Team 配置文档

**配置日期**: 2026-04-01  
**Agent Leader**: 强国小马（chief-agent）  
**团队规模**: 5 个专业 Agent + 1 个 Leader

---

## 👥 团队成员与技能映射

### 📋 1. 运营管理 (ops-agent-001)

**职责**: 业务流程管理、数据分析、资源协调、项目跟进

**已安装技能**:
| 技能名称 | 版本 | 用途 |
|---------|------|------|
| `proactive-agent` | 3.1.0 | 主动任务管理 |
| `agent-team-orchestration` | 1.0.0 | 团队协调 |
| `project-management-2` | 0.1.0 | 项目管理 |

**SLA**: 响应 60s, 完成率 95%

---

### 💰 2. 财务顾问 (finance-agent-001)

**职责**: 财务分析、预算管理、成本控制、合规审查

**已安装技能**:
| 技能名称 | 版本 | 用途 |
|---------|------|------|
| `finance-report-analyzer` | 1.2.0 | 财务报告分析 |
| `security-auditor` | 1.0.0 | 安全审计 |

**SLA**: 响应 60s, 准确率 99%

---

### ⚖️ 3. 法务顾问 (legal-agent-001)

**职责**: 合同审查、法律咨询、风险防控、纠纷处理

**已安装技能**:
| 技能名称 | 版本 | 用途 |
|---------|------|------|
| `legal-advisor` | 2.0.1 | 法律咨询 |
| `agent-commercial-contract` | 1.0.0 | 商业合同审查 |

**SLA**: 响应 30s, 准确率 98%

---

### ✍️ 4. 文案撰稿 (copywriter-agent-001)

**职责**: 营销文案、产品描述、品牌故事、内容策划

**已安装技能**:
| 技能名称 | 版本 | 用途 |
|---------|------|------|
| `content-writer` | latest | 内容写作 |
| `ai-copywriter` | latest | AI 文案生成 |
| `proactive-agent` | 3.1.0 | 主动创作 |

**SLA**: 响应 120s, 通过率 90%

---

### 🎨 5. 平面设计 (design-agent-001)

**职责**: 视觉设计、图片生成、视频制作、多媒体内容

**已安装技能**:
| 技能名称 | 版本 | 用途 |
|---------|------|------|
| `graphic-design` | latest | 平面设计 |
| `designer` | latest | 设计工具 |
| `minimax-multimodal` | 1.0.1 | 多媒体生成 |
| `video-generation-minimax` | 1.0.0 | 视频生成 |
| `minimax-speech` | 1.0.0 | 语音合成 |
| `minimax-tts-cn` | 1.0.0 | 中文 TTS |

**SLA**: 图片 300s, 视频 1800s, 满意度 85%

---

## 🔄 工作流程

```
┌─────────────┐
│   用户请求   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  小马 (Leader) │ ← 接收需求、分析任务、路由分发、汇总结果
└──────┬──────┘
       │
       ├──────────┬──────────┬──────────┬──────────┐
       │          │          │          │          │
       ▼          ▼          ▼          ▼          ▼
  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
  │ 运营管理 │ │ 财务顾问 │ │ 法务顾问 │ │ 文案撰稿 │ │ 平面设计 │
  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘
```

---

## 📊 技能总览

### 已安装技能统计

| 类别 | 数量 | 技能列表 |
|------|------|---------|
| **Agent 核心** | 3 | proactive-agent, self-improving-agent, agent-team-orchestration |
| **运营管理** | 2 | project-management-2, agent-team-orchestration |
| **财务** | 1 | finance-report-analyzer |
| **法务** | 2 | legal-advisor, agent-commercial-contract |
| **文案** | 2 | content-writer, ai-copywriter |
| **设计** | 2 | graphic-design, designer |
| **MiniMax 套件** | 9 | docx/xlsx/pdf/mcp/speech/tts/multimodal/video/usage |
| **其他工具** | 16 | security, memory, search, coding 等 |

**总技能数**: 37 个

---

## 🎯 使用示例

### 场景 1: 合同审查
```
用户："小马，帮我看看这份合同有没有法律风险"
→ 路由给 → 法务顾问 (legal-agent-001)
→ 使用技能 → legal-advisor + agent-commercial-contract
→ 输出 → 合同审查报告 + 风险点列表
```

### 场景 2: 财务分析
```
用户："小马，分析一下上季度的财务状况"
→ 路由给 → 财务顾问 (finance-agent-001)
→ 使用技能 → finance-report-analyzer
→ 输出 → 财务分析报告 + 建议
```

### 场景 3: 营销文案
```
用户："小马，帮我想一个新产品上市的文案"
→ 路由给 → 文案撰稿 (copywriter-agent-001)
→ 使用技能 → content-writer + ai-copywriter
→ 输出 → 多版本文案方案
```

### 场景 4: 设计需求
```
用户："小马，帮我设计一个产品宣传海报"
→ 路由给 → 平面设计 (design-agent-001)
→ 使用技能 → graphic-design + minimax-multimodal
→ 输出 → 海报设计稿
```

### 场景 5: 项目协调
```
用户："小马，帮我安排下周的项目会议"
→ 路由给 → 运营管理 (ops-agent-001)
→ 使用技能 → project-management-2
→ 输出 → 会议安排 + 参会人员 + 议程
```

---

## ⚙️ 配置说明

### API Key 配置

```bash
# MiniMax API Key（已配置）
export MINIMAX_API_KEY="sk-api-..."

# 位置：~/.bashrc
```

### Agent 路由规则

小马（chief-agent）根据以下规则路由：

| 关键词 | 路由目标 |
|-------|---------|
| 合同、法律、风险、合规 | 法务顾问 |
| 财务、预算、成本、报表 | 财务顾问 |
| 文案、内容、写作、营销 | 文案撰稿 |
| 设计、图片、视频、海报 | 平面设计 |
| 项目、会议、协调、流程 | 运营管理 |
| 其他 | 小马直接处理 |

---

## 📈 SLA 监控

| Agent | 响应时间 | 完成率/准确率 | 监控方式 |
|-------|---------|-------------|---------|
| 运营管理 | 60s | 95% | 任务跟踪 |
| 财务顾问 | 60s | 99% | 复核机制 |
| 法务顾问 | 30s | 98% | 专业审核 |
| 文案撰稿 | 120s | 90% | 用户反馈 |
| 平面设计 | 300s/1800s | 85% | 满意度调查 |

---

## 🔧 维护与更新

### 技能更新
```bash
# 更新所有技能
clawhub update

# 更新特定技能
clawhub update <skill-name>
```

### 技能添加
```bash
# 搜索新技能
clawhub search <keyword>

# 安装技能
clawhub install <skill-name> --force
```

### 监控用量
```bash
# 使用 MiniMax 用量监控
minimax-usage
```

---

## 📝 待办事项

- [ ] 测试每个 Agent 的功能
- [ ] 配置自动化路由规则
- [ ] 设置 SLA 监控告警
- [ ] 创建 Agent 使用文档
- [ ] 定期审查技能更新

---

**配置完成时间**: 2026-04-01 02:30 GMT+8  
**配置耗时**: 约 20 分钟

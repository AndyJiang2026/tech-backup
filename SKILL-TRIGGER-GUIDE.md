# 🎯 强国小马 Agent Team - 技能触发指南

**版本**: 1.0  
**创建时间**: 2026-04-01  
**用途**: 帮助用户快速了解如何触发各技能，让技能真正发挥作用

---

## 📖 使用说明

### 🐴 核心原则

**你只需要告诉小马（chief-agent）你的需求**，小马会自动：
1. 理解任务类型
2. 路由到最合适的 Agent
3. 调用对应技能
4. 汇总结果回复你

**不需要**记住技能名称，**只需要**用自然语言描述需求！

---

## 🗂️ 技能触发速查表

### 📧 邮件管理（porteden-email）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "查看今天的邮件" | 小马 → porteden-email | `porteden email messages --today` |
| "有没有重要邮件" | 小马 → porteden-email | `porteden email messages --unread` |
| "搜索包含合同的邮件" | 小马 → porteden-email | `porteden email messages -q "合同"` |
| "回复刚才那封邮件" | 小马 → porteden-email | `porteden email reply <id>` |
| "帮我把这个发给张三" | 小马 → porteden-email | `porteden email send --to` |

**前置配置**: `porteden auth login`（首次使用）

---

### 📱 社交媒体（social-media-scheduler）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "把这篇文案发微博" | 小马 → social-media-scheduler | 发布到微博 |
| "排期发布到公众号" | 小马 → social-media-scheduler | 定时发布 |
| "明天上午 10 点发这条" | 小马 → social-media-scheduler | 定时任务 |
| "看看已排期的内容" | 小马 → social-media-scheduler | 查看排期 |

**前置配置**: 绑定微博/公众号 API

---

### 🤝 客户管理（crm-manager）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "记录和张总的会议" | 小马 → crm-manager | 创建客户记录 |
| "查找李总的联系方式" | 小马 → crm-manager | 搜索客户 |
| "更新王总的跟进状态" | 小马 → crm-manager | 更新记录 |
| "下周要联系哪些客户" | 小马 → crm-manager | 查询待跟进 |

**前置配置**: 自定义 CRM 字段（可选）

---

### 📊 数据分析（analyze / data-analyst-pro）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "分析这份销售数据" | 小马 → 研究分析 Agent | `analyze` |
| "上个月业绩怎么样" | 小马 → 研究分析 Agent | `data-analyst-pro` |
| "画个趋势图" | 小马 → 研究分析 Agent | `analyze` + 可视化 |
| "找出异常数据" | 小马 → 研究分析 Agent | `data-analyst-pro` |

---

### 📝 内容创作（content-writer / ai-copywriter）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "写个产品描述" | 小马 → 文案撰稿 Agent | `ai-copywriter` |
| "帮我想个广告语" | 小马 → 文案撰稿 Agent | `content-writer` |
| "写篇品牌故事" | 小马 → 文案撰稿 Agent | `content-writer` |
| "优化这段文案" | 小马 → 文案撰稿 Agent | `ai-copywriter` |

---

### 📋 内容摘要（summarize）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "总结一下这篇文章" | 小马 → 文案撰稿 Agent | `summarize` |
| "会议纪要整理一下" | 小马 → 文案撰稿 Agent | `summarize` |
| "太长不看，给个摘要" | 小马 → 文案撰稿 Agent | `summarize` |
| "3 句话说完重点" | 小马 → 文案撰稿 Agent | `summarize` |

---

### 🌐 网络搜索（searxng / minimax-mcp）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "查一下 XX 的最新消息" | 小马/研究分析 | `searxng`（优先） |
| "搜索 XX 的研究论文" | 小马 → 研究分析 | `scholar-search` |
| "找一下 GitHub 上的 XX 项目" | 小马 → 研究分析 | `github-search` |
| "XX 是什么意思" | 小马 | `minimax-mcp` |

---

### 🎨 平面设计（graphic-design / designer）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "设计个 Logo" | 小马 → 平面设计 Agent | `graphic-design` |
| "做张宣传海报" | 小马 → 平面设计 Agent | `designer` |
| "生成产品图片" | 小马 → 平面设计 Agent | `openai-image-gen` |
| "改一下这个设计" | 小马 → 平面设计 Agent | `graphic-design` |

---

### 🎬 视频制作（video-generation-minimax）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "做个产品宣传视频" | 小马 → 平面设计 Agent | `video-generation-minimax` |
| "把文案转成视频" | 小马 → 平面设计 Agent | `minimax-multimodal` |
| "生成讲解视频" | 小马 → 平面设计 Agent | `video-generation-minimax` |

---

### 📄 文档生成（minimax-docx-pro / xlsx-pro / pdf-pro）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "生成 Word 文档" | 小马 | `minimax-docx-pro` |
| "做个 Excel 表格" | 小马 | `minimax-xlsx-pro` |
| "创建 PDF 报告" | 小马 | `minimax-pdf-pro` |
| "导出为 PDF" | 小马 | `minimax-pdf-pro` |

---

### 📞 语音合成（minimax-speech / minimax-tts-cn）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "把这段文字读出来" | 小马 → 平面设计 Agent | `minimax-tts-cn` |
| "生成中文语音" | 小马 → 平面设计 Agent | `minimax-tts-cn` |
| "生成英文语音" | 小马 → 平面设计 Agent | `minimax-speech` |
| "用语音讲故事" | 小马 → 平面设计 Agent | `sag` |

---

### ⚖️ 法务咨询（legal-advisor / agent-commercial-contract）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "审查这份合同" | 小马 → 法务顾问 Agent | `agent-commercial-contract` |
| "有什么法律风险" | 小马 → 法务顾问 Agent | `legal-advisor` |
| "这个条款合法吗" | 小马 → 法务顾问 Agent | `legal-advisor` |
| "帮我修改合同" | 小马 → 法务顾问 Agent | `agent-commercial-contract` |

---

### 💰 财务分析（finance-report-analyzer）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "分析财务报表" | 小马 → 财务顾问 Agent | `finance-report-analyzer` |
| "预算够吗" | 小马 → 财务顾问 Agent | `finance-report-analyzer` |
| "成本怎么控制" | 小马 → 财务顾问 Agent | `finance-report-analyzer` |
| "这个项目赚钱吗" | 小马 → 财务顾问 Agent | `finance-report-analyzer` |

---

### 📈 项目管理（project-management-2）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "制定项目计划" | 小马 → 运营管理 Agent | `project-management-2` |
| "跟踪项目进度" | 小马 → 运营管理 Agent | `project-management-2` |
| "分配任务给张三" | 小马 → 运营管理 Agent | `project-management-2` |
| "项目延期了怎么办" | 小马 → 运营管理 Agent | `project-management-2` |

---

### 🔍 市场调研（market-research / ai-researcher）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "调研 XX 市场" | 小马 → 研究分析 Agent | `market-research` |
| "竞争对手有哪些" | 小马 → 研究分析 Agent | `competitor-analyst` |
| "行业趋势分析" | 小马 → 研究分析 Agent | `ai-researcher` |
| "用户画像是什么" | 小马 → 研究分析 Agent | `market-research` |

---

### 🧠 记忆系统（memory-tiering / elite-longterm-memory）

| 你说 | 小马路由 | 触发技能 |
|------|---------|---------|
| "记住这个" | 小马自动 | `elite-longterm-memory` |
| "我之前说过 XX 吗" | 小马自动 | `memory-tiering` |
| "查找之前的讨论" | 小马自动 | `elite-longterm-memory` |
| "总结一下我们的进展" | 小马自动 | 记忆系统 |

**自动触发**，无需手动调用

---

## 🎯 复杂任务示例

### 示例 1: 新产品上市

```
你："小马，我们要推出新产品，需要全套上市方案"

小马自动分解：
├─ 市场调研 → 研究分析 Agent (market-research)
├─ 竞品分析 → 研究分析 Agent (competitor-analyst)
├─ 营销文案 → 文案撰稿 Agent (ai-copywriter)
├─ 宣传海报 → 平面设计 Agent (graphic-design)
├─ 宣传视频 → 平面设计 Agent (video-generation-minimax)
├─ 预算评估 → 财务顾问 Agent (finance-report-analyzer)
└─ 项目计划 → 运营管理 Agent (project-management-2)

小马 → 汇总所有结果 → 输出完整上市方案
```

### 示例 2: 合同审查 + 邮件发送

```
你："小马，审查这份合同，没问题的话发给法务部"

小马自动处理：
├─ 合同审查 → 法务顾问 Agent (agent-commercial-contract)
├─ 风险评估 → 法务顾问 Agent (legal-advisor)
└─ 邮件发送 → porteden-email

小马 → 输出审查结果 + 邮件发送确认
```

### 示例 3: 会议纪要 + 客户跟进

```
你："小马，整理昨天的会议纪要，并更新客户跟进记录"

小马自动处理：
├─ 会议录音转文字 → 平面设计 Agent (minimax-speech)
├─ 内容摘要 → 文案撰稿 Agent (summarize)
├─ 客户记录更新 → crm-manager
└─ 纪要文档生成 → 小马 (minimax-docx-pro)

小马 → 输出会议纪要 + CRM 更新确认
```

---

## 🚀 最佳实践

### ✅ 这样做

1. **直接说需求** - "帮我写个产品描述"
2. **提供上下文** - "这是我们的新产品，主打年轻人群体..."
3. **指定格式** - "用表格形式展示"
4. **设定时限** - "今天下班前给我"
5. **反馈调整** - "这个风格不对，要更活泼一点"

### ❌ 避免这样

1. ~~直接调用技能名~~ - "执行 summarize 技能"（应该："总结一下"）
2. ~~模糊描述~~ - "帮我弄一下那个"（应该："帮我整理昨天的会议纪要"）
3. ~~一次性多个需求~~ - "写文案、做图、发微博、查数据"（应该分条说）

---

## 📊 技能调用统计（可选）

小马会自动记录各技能使用频率，帮助你优化：

```bash
# 查看技能使用情况
clawhub run skill-vetter
```

---

## 🔧 高级配置

### 自定义触发词

如果你想添加自定义触发词，编辑：
```
/home/admin/.openclaw/workspace-chief-agent/SKILL-TRIGGER-CONFIG.md
```

### 调整路由规则

如果你想改变某个任务的默认路由 Agent：
```
编辑 SKILL-DIRECTORY.md 中的"任务路由矩阵"
```

### 添加新技能触发

发现新技能后，更新本文档：
1. 添加技能到对应分类
2. 添加触发示例
3. 更新任务路由矩阵

---

## 📞 快速帮助

**忘记技能怎么触发？**
- 查看本文档
- 或直接问小马："这个需求你会怎么处理？"

**技能没被触发？**
- 检查前置配置（如 API Key）
- 确认描述清晰
- 查看 OPTIMIZATION-TODO.md

**需要新技能？**
- 告诉小马你的需求
- 小马会搜索并推荐合适技能
- 执行 `clawhub install <skill-name>`

---

**文档维护**: 强国小马（chief-agent）  
**最后更新**: 2026-04-01

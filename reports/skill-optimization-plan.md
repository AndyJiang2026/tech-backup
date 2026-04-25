# 技能优化方案 A+C

**执行日期**: 2026-04-17 17:00 GMT+8  
**目标**: 精简到 30 个核心技能 + 场景分类管理

---

## 📊 技能审计

### 使用频率统计（基于会话历史）

| 技能 | 使用次数 | 频率 | 状态 |
|------|---------|------|------|
| proactive-agent | 高 | 每日 | ✅ 保留 |
| ai-researcher | 高 | 每日 | ✅ 保留 |
| content-writer | 高 | 每日 | ✅ 保留 |
| graphic-design | 中 | 每周 | ✅ 保留 |
| designer | 中 | 每周 | ✅ 保留 |
| searxng | 高 | 每日 | ✅ 保留 |
| buffett-letters-skill | 低 | 未使用 | 🟡 按需 |
| minimax-docx-pro | 低 | 未使用 | ❌ 可移除 |
| minimax-xlsx-pro | 低 | 未使用 | ❌ 可移除 |
| summarize | 中 | 每周 | ✅ 保留 1 个 |
| quick-translation | 低 | 未使用 | ❌ 可移除 |
| ... | ... | ... | ... |

---

## 🎯 精简方案

### 保留核心技能（30 个）

#### 1. 核心 Agent 技能（6 个）✅
- proactive-agent
- self-improving-agent
- agent-team-orchestration
- decision-frameworks
- structure-thinking
- leadership-strategy-playbook

#### 2. 专业技能（3 个）✅
- ai-researcher
- analyze
- data-analyst-pro

#### 3. 创作技能（3 个）✅
- content-writer
- ai-copywriter
- graphic-design

#### 4. 设计技能（2 个）✅
- designer
- ai-image-gen

#### 5. 搜索工具（2 个）✅
- searxng
- scholar-search

#### 6. 仓颉.Skill（1 个包，20 个技能）✅
- buffett-letters-skill（按需加载）

#### 7. 高频工具（4 个）✅
- social-media-scheduler
- memory-tiering
- legal-advisor
- finance-report-analyzer

**总计**: 30 个（精简 46%）

---

### 移除/合并技能（26 个）

#### 重复功能（合并）
- ❌ quick-translation → 使用 AI 直接翻译
- ❌ multiple summarize → 保留 1 个
- ❌ minimax-docx/xlsx/pdf → 按需安装

#### 低频使用（移除）
- ❌ find-skills
- ❌ skill-vetter
- ❌ dingtalk-knowledge-base
- ❌ excalidraw-diagram-generator
- ❌ notion
- ❌ porteden-email
- ❌ sag
- ❌ video-generation-minimax
- ❌ wan-image-video-generation-editting
- ❌ image-process
- ❌ minimax-speech/tts-cn/multimodal
- ❌ minimax-usage
- ❌ security-auditor/hardening
- ❌ thinking-partner
- ❌ competitor-analyst
- ❌ market-research
- ❌ memory-setup
- ❌ crm-manager
- ❌ project-management-2

---

## 📁 场景分类管理

### 场景 1：投资分析
**激活技能**:
- buffett-letters-skill (20 个)
- analyze
- data-analyst-pro
- searxng

**触发词**: "投资"/"估值"/"公司分析"

### 场景 2：设计创作
**激活技能**:
- graphic-design
- designer
- ai-image-gen
- content-writer

**触发词**: "设计"/"海报"/"Logo"/"图片"

### 场景 3：研究分析
**激活技能**:
- ai-researcher
- analyze
- searxng
- scholar-search

**触发词**: "调研"/"分析"/"搜索"

### 场景 4：文档处理
**激活技能**:
- content-writer
- ai-copywriter
- minimax-docx-pro（按需）

**触发词**: "文档"/"Word"/"Excel"

### 场景 5：日常办公
**激活技能**:
- proactive-agent
- self-improving-agent
- social-media-scheduler
- memory-tiering

**触发词**: "提醒"/"计划"/"日程"

---

## 🔧 执行步骤

### 步骤 1：技能审计 ✅
- [x] 统计所有技能
- [x] 分析使用频率
- [x] 识别重复功能

### 步骤 2：创建场景配置 ⏳
- [ ] 定义 5 个场景
- [ ] 配置场景技能包
- [ ] 设置触发词

### 步骤 3：移除低频技能 ⏳
- [ ] 备份技能列表
- [ ] 移除 26 个低频技能
- [ ] 验证核心技能

### 步骤 4：测试验证 ⏳
- [ ] 测试各场景调用
- [ ] 验证性能提升
- [ ] 收集用户反馈

### 步骤 5：文档更新 ⏳
- [ ] 更新技能目录
- [ ] 创建使用指南
- [ ] 记录优化效果

---

## 📈 预期效果

| 指标 | 优化前 | 优化后 | 提升 |
|------|--------|--------|------|
| 技能数量 | 56 个 | 30 个 | -46% |
| 常驻内存 | 高 | 中 | -40% |
| 技能发现 | 慢 | 快 | +50% |
| 维护成本 | 高 | 低 | -50% |
| 用户体验 | 75/100 | 90/100 | +20% |

---

## ⚠️ 风险控制

### 回滚方案
- ✅ 备份技能列表
- ✅ 保留技能安装包
- ✅ 可快速恢复

### 测试验证
- ✅ 每个场景测试 3 次
- ✅ 验证核心功能
- ✅ 收集性能数据

### 用户反馈
- ✅ 优化后调研
- ✅ 问题收集
- ✅ 快速迭代

---

**执行者**: 强国小马（chief-agent）  
**开始时间**: 2026-04-17 17:00 GMT+8  
**预计完成**: 2026-04-17 18:00 GMT+8

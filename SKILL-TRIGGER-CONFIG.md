# 🎯 技能触发配置

**用途**: 配置小马自动识别用户需求并路由到对应技能的规则

---

## 📋 触发词映射表

### 邮件管理（porteden-email）

```yaml
触发词:
  - 邮件
  - email
  - 查看邮件
  - 查收邮件
  - 回复邮件
  - 发送邮件
  - 转发邮件
  - 重要邮件
  - 未读邮件
  - 搜索邮件

路由：porteden-email
前置条件：porteden auth login
```

### 社交媒体（social-media-scheduler）

```yaml
触发词:
  - 微博
  - 公众号
  - 发布
  - 排期
  - 定时发布
  - 社交媒体
  - 朋友圈
  - 小红书
  - 抖音

路由：social-media-scheduler
前置条件：绑定平台 API
```

### 客户管理（crm-manager）

```yaml
触发词:
  - 客户
  - CRM
  - 跟进
  - 客户记录
  - 联系记录
  - 客户信息
  - 销售机会
  - 商机

路由：crm-manager
前置条件：无（可选：自定义字段）
```

### 数据分析（analyze / data-analyst-pro）

```yaml
触发词:
  - 分析
  - 数据
  - 报表
  - 趋势
  - 图表
  - 可视化
  - 业绩
  - 销售数据
  - 异常

路由：研究分析 Agent
技能：analyze, data-analyst-pro
```

### 内容创作（content-writer / ai-copywriter）

```yaml
触发词:
  - 写
  - 文案
  - 描述
  - 广告语
  - 品牌故事
  - 优化
  - 润色
  - 改写

路由：文案撰稿 Agent
技能：content-writer, ai-copywriter
```

### 内容摘要（summarize）

```yaml
触发词:
  - 总结
  - 摘要
  - 概括
  - 太长不看
  - TLDR
  - 会议纪要
  - 重点

路由：文案撰稿 Agent
技能：summarize
```

### 网络搜索（searxng / minimax-mcp）

```yaml
触发词:
  - 搜索
  - 查找
  - 查询
  - 最新消息
  - 调研
  - 了解
  - 是什么意思

路由：小马 或 研究分析 Agent
技能：searxng（优先）, minimax-mcp
```

### 平面设计（graphic-design / designer）

```yaml
触发词:
  - 设计
  - Logo
  - 海报
  - 图片
  - 图像
  - 视觉
  - 美化
  - 作图

路由：平面设计 Agent
技能：graphic-design, designer, openai-image-gen
```

### 视频制作（video-generation-minimax）

```yaml
触发词:
  - 视频
  - 影片
  - 剪辑
  - 生成视频
  - 宣传视频
  - 讲解视频

路由：平面设计 Agent
技能：video-generation-minimax, minimax-multimodal
```

### 文档生成（minimax-docx-pro / xlsx-pro / pdf-pro）

```yaml
触发词:
  - Word
  - Excel
  - PDF
  - 文档
  - 表格
  - 报告
  - 导出

路由：小马
技能：minimax-docx-pro, minimax-xlsx-pro, minimax-pdf-pro
```

### 语音合成（minimax-speech / minimax-tts-cn）

```yaml
触发词:
  - 语音
  - 朗读
  - TTS
  - 配音
  - 读出来
  - 声音
  - 讲故事

路由：平面设计 Agent
技能：minimax-tts-cn, minimax-speech, sag
```

### 法务咨询（legal-advisor / agent-commercial-contract）

```yaml
触发词:
  - 合同
  - 法律
  - 法务
  - 风险
  - 条款
  - 审查
  - 合法
  - 纠纷

路由：法务顾问 Agent
技能：legal-advisor, agent-commercial-contract
```

### 财务分析（finance-report-analyzer）

```yaml
触发词:
  - 财务
  - 预算
  - 成本
  - 报表
  - 赚钱
  - 亏损
  - 投资
  - 收益

路由：财务顾问 Agent
技能：finance-report-analyzer
```

### 项目管理（project-management-2）

```yaml
触发词:
  - 项目
  - 计划
  - 进度
  - 任务
  - 分配
  - 延期
  - 跟进

路由：运营管理 Agent
技能：project-management-2
```

### 市场调研（market-research / ai-researcher）

```yaml
触发词:
  - 调研
  - 市场
  - 竞品
  - 对手
  - 行业
  - 趋势
  - 用户画像

路由：研究分析 Agent
技能：market-research, ai-researcher, competitor-analyst
```

---

## 🔄 路由决策树

```
用户需求
  │
  ├─ 含"邮件/email" → porteden-email
  ├─ 含"微博/公众号/发布" → social-media-scheduler
  ├─ 含"客户/CRM/跟进" → crm-manager
  ├─ 含"合同/法律/法务" → 法务顾问 Agent
  ├─ 含"财务/预算/成本" → 财务顾问 Agent
  ├─ 含"设计/图片/Logo" → 平面设计 Agent
  ├─ 含"视频/影片" → 平面设计 Agent
  ├─ 含"分析/数据/报表" → 研究分析 Agent
  ├─ 含"调研/市场/竞品" → 研究分析 Agent
  ├─ 含"写/文案/广告" → 文案撰稿 Agent
  ├─ 含"总结/摘要/概括" → 文案撰稿 Agent
  ├─ 含"项目/计划/进度" → 运营管理 Agent
  ├─ 含"Word/Excel/PDF" → 小马（文档生成）
  ├─ 含"搜索/查找/查询" → 小马/研究分析（搜索）
  └─ 其他 → 小马（智能判断）
```

---

## ⚙️ 自动路由配置

### 小马路由逻辑

```python
# 伪代码示例
def route_task(user_input):
    # 1. 提取关键词
    keywords = extract_keywords(user_input)
    
    # 2. 匹配触发词
    for trigger in TRIGGER_MAP:
        if any(keyword in trigger.keywords for keyword in keywords):
            return trigger.route
    
    # 3. 语义分析（备用）
    intent = analyze_intent(user_input)
    return intent.suggested_agent
    
    # 4. 默认路由
    return "chief-agent"  # 小马自己处理
```

### 多技能协同

```python
# 复杂任务分解
def decompose_task(user_input):
    subtasks = []
    
    if "新产品上市" in user_input:
        subtasks = [
            {"agent": "研究分析", "skill": "market-research"},
            {"agent": "研究分析", "skill": "competitor-analyst"},
            {"agent": "文案撰稿", "skill": "ai-copywriter"},
            {"agent": "平面设计", "skill": "graphic-design"},
            {"agent": "财务顾问", "skill": "finance-report-analyzer"},
        ]
    
    return subtasks
```

---

## 📊 技能使用统计

### 追踪指标

```yaml
指标:
  - 技能调用次数
  - 平均响应时间
  - 用户满意度
  - 任务完成率
  - 路由准确率
```

### 查看统计

```bash
# 查看技能使用情况
clawhub run skill-vetter

# 查看 MiniMax 用量
cd /home/admin/.openclaw/workspace/skills/minimax-usage
./minimax-usage.sh
```

---

## 🔧 配置维护

### 添加新触发词

1. 编辑 `SKILL-TRIGGER-CONFIG.md`
2. 在对应技能下添加触发词
3. 测试路由是否生效

### 调整路由规则

1. 编辑 `SKILL-DIRECTORY.md` 中的"任务路由矩阵"
2. 更新路由决策树
3. 测试新路由

### 优化建议

- 定期查看技能使用频率
- 收集用户反馈
- 调整不准确的触发词
- 添加新技能触发规则

---

## 🎯 最佳实践

### 触发词设计原则

1. **自然语言** - 用户实际会说的话
2. **覆盖全面** - 同义词、近义词都包含
3. **避免歧义** - 不与其他技能冲突
4. **简洁明了** - 容易记忆和维护

### 路由优化原则

1. **专业优先** - 专业任务路由到专业 Agent
2. **简单直管** - 简单任务小马直接处理
3. **减少层级** - 最多 2 层路由
4. **快速响应** - 优先选择响应快的技能

---

**维护者**: 强国小马（chief-agent）  
**最后更新**: 2026-04-01

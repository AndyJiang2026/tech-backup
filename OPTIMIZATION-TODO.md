# 🐴 强国小马 Agent Team - 优化执行清单

**创建时间**: 2026-04-01  
**状态**: 🔄 进行中

---

## ✅ 已完成

### 1️⃣ 技能精简
- [x] 移除 `summarize-pro`（功能与 `summarize` 重叠）
- [x] 标注 TTS 技能合并使用策略
- [x] 更新 SKILL-DIRECTORY.md

### 2️⃣ 能力补充
- [x] 安装 `porteden-email`（邮件管理）
- [x] 安装 `social-media-scheduler`（社交媒体排期）
- [x] 安装 `crm-manager`（客户关系管理）
- [x] 更新技能目录文档

### 3️⃣ 性能调优
- [x] 确认 MiniMax API Key 已配置（`~/.bashrc`）
- [x] 安装 porteden CLI 工具（v0.2.1）
- [x] 创建 minimax-usage 配置模板
- [x] 配置 searxng 为优先搜索引擎

### 4️⃣ 流程优化
- [x] 更新任务路由矩阵
- [x] 简化路由层级（小马直管简单任务）
- [x] 创建 OPTIMIZATION-REPORT.md

---

## 🔄 进行中

### 配置待办
- [ ] **配置 PortEden Email** - 需要用户浏览器登录或配置 PE_API_KEY
  - 命令：`porteden auth login`
  - 或设置环境变量：`PE_API_KEY`
  
- [ ] **配置 MiniMax Usage 监控** - 需要 GroupId
  - 位置：`/home/admin/.openclaw/workspace/skills/minimax-usage/.env`
  - 获取 GroupId：https://platform.minimax.io/user-center/basic-information

- [ ] **配置社交媒体账户** - social-media-scheduler 需要绑定平台 API
  - 微博/公众号 API 密钥

- [ ] **配置 CRM 字段** - crm-manager 需要自定义客户字段
  - 模板位置：`/home/admin/.openclaw/workspace/skills/crm-manager/crm-template.csv`

---

## 📋 待办（低优先级）

- [ ] 定期执行 `clawhub update`（建议每周）
- [ ] 监控各 Agent 响应时间和质量
- [ ] 收集用户反馈优化路由规则

---

## 🎯 新技能快速测试

### 测试邮件功能
```bash
# 1. 登录 PortEden（首次使用）
porteden auth login

# 2. 验证登录状态
porteden auth status

# 3. 查看今日邮件
porteden email messages --today -jc
```

### 测试用量监控
```bash
# 1. 配置 .env 文件
cd /home/admin/.openclaw/workspace/skills/minimax-usage
cp .env.example .env
# 编辑 .env 填入 MINIMAX_CODING_API_KEY 和 MINIMAX_GROUP_ID

# 2. 执行监控
./minimax-usage.sh
```

### 测试 CRM
```bash
# 查看 CRM 模板
cat /home/admin/.openclaw/workspace/skills/crm-manager/crm-template.csv
```

---

## 📊 技能清单（优化后）

**总数**: 44 个技能

| 类别 | 数量 | 变更 |
|------|------|------|
| Agent 核心 | 6 | - |
| 小马专属 | 4 | - |
| 运营管理 | 5 | - |
| 财务顾问 | 3 | - |
| 法务顾问 | 3 | - |
| 文案撰稿 | 4 | -1（精简） |
| 平面设计 | 8 | - |
| 研究分析 | 4 | - |
| MiniMax 套件 | 9 | - |
| 记忆系统 | 3 | - |
| 搜索工具 | 3 | - |
| 其他工具 | 4 | - |
| **新增能力** | **3** | **+3** |

---

**最后更新**: 2026-04-01 07:00 GMT+8  
**维护者**: 强国小马（chief-agent）

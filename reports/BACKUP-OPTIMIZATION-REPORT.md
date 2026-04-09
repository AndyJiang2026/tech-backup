# 📦 异地备份优化方案实施报告

**创建时间**: 2026-04-09 15:45 GMT+8  
**执行人**: 强国小马（chief-agent）  
**方案**: 方案 2（阿里云 OSS）+ 方案 3（百炼知识库）

---

## 📊 备份机制总览

### 当前备份架构

```
┌─────────────────────────────────────────────────┐
│         强国小马备份架构 v2.0                    │
├─────────────────────────────────────────────────┤
│                                                 │
│  本地工作区                                      │
│  └── workspace-chief-agent/                     │
│       │                                         │
│       ├─ Git 实时备份 ─────→ GitHub             │
│       │                     (tech-backup)       │
│       │                                         │
│       ├─ OSS 定时备份 ─────→ 阿里云 OSS         │
│       │   (每天 3:00)       (qiangguo-xiaoma)   │
│       │                                         │
│       └─ 知识库同步 ───────→ 百炼知识库         │
│           (每周日 2:00)     (强国小马知识库)     │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## ✅ 已完成工作

### 1️⃣ 脚本开发

| 脚本 | 位置 | 状态 | 用途 |
|------|------|------|------|
| **oss-backup.sh** | `/home/admin/.openclaw/scripts/` | ✅ 已创建 | OSS 自动备份 |
| **health-check-full.sh** | `/home/admin/.openclaw/scripts/` | ✅ 已创建 | 全面健康检查 |
| **auto-backup.sh** | `workspace-chief-agent/` | ✅ 已更新 | 集成 OSS 备份 |

### 2️⃣ 配置文档

| 文档 | 位置 | 状态 | 用途 |
|------|------|------|------|
| **OSS-SETUP-GUIDE.md** | `/home/admin/.openclaw/scripts/` | ✅ 已创建 | OSS 配置指南 |
| **BAILIAN-KNOWLEDGE-SETUP.md** | `/home/admin/.openclaw/scripts/` | ✅ 已创建 | 百炼知识库指南 |
| **BACKUP-OPTIMIZATION-REPORT.md** | `/home/admin/.openclaw/reports/` | ✅ 已创建 | 本报告 |

### 3️⃣ Git 提交

| Commit | 说明 | 文件数 |
|--------|------|--------|
| `05e8bcb` | 📦 添加 OSS 备份和百炼知识库配置指南 | 1 |
| `1db76fd` | 🧠 充实 MEMORY.md 长期记忆 | 1 |
| `114f0ee` | 📊 添加系统健康检查报告 | 8 |

---

## 📋 方案 2: 阿里云 OSS 备份

### 配置步骤

#### 步骤 1: 安装 ossutil

```bash
wget https://gosspublic.alicdn.com/ossutil/install.sh
bash install.sh
ossutil64 --version
```

#### 步骤 2: 配置凭证

```bash
ossutil64 config
```

输入：
- Endpoint: `oss-cn-hangzhou.aliyuncs.com`
- AccessKey ID: `<你的 AccessKey ID>`
- AccessKey Secret: `<你的 AccessKey Secret>`

#### 步骤 3: 创建 Bucket

```bash
# 方式 A: 控制台创建
访问：https://oss.console.aliyun.com/
创建 Bucket: qiangguo-xiaoma-backup

# 方式 B: 命令行创建
ossutil64 mb oss://qiangguo-xiaoma-backup
ossutil64 bucket-versioning oss://qiangguo-xiaoma-backup enable
```

#### 步骤 4: 测试备份

```bash
/home/admin/.openclaw/scripts/oss-backup.sh
```

#### 步骤 5: 配置定时任务

```bash
crontab -e
# 添加：每天凌晨 3 点执行 OSS 备份
0 3 * * * /home/admin/.openclaw/scripts/oss-backup.sh >> /var/log/oss-backup.log 2>&1
```

### 备份内容

| 类型 | 路径 | OSS 位置 | 频率 |
|------|------|---------|------|
| **Agent 配置** | `agents/business-team/` | `oss://.../openclaw/agents/` | 每日 |
| **本地备份** | `backup/` | `oss://.../openclaw/local-backup/` | 每日 |
| **核心文档** | `*.md` | `oss://.../openclaw/docs/` | 每日 |
| **业务文档** | `docs/` | `oss://.../openclaw/docs/business/` | 每日 |
| **财务报告** | `finance/` | `oss://.../openclaw/docs/finance/` | 每日 |
| **法务文档** | `legal-compliance/` | `oss://.../openclaw/docs/legal/` | 每日 |

### 费用估算

| 项目 | 用量 | 单价 | 月费用 |
|------|------|------|--------|
| **存储费** | 1GB | ¥0.12/GB | ¥0.12 |
| **版本控制** | 2GB | ¥0.12/GB | ¥0.24 |
| **请求费** | 1 万次 | ¥0.01/万 | ¥0.01 |
| **流量费** | 0GB（内网） | ¥0 | ¥0 |

**总计**: **¥0.37/月**

---

## 📚 方案 3: 百炼知识库

### 配置步骤

#### 步骤 1: 访问百炼控制台

访问：https://bailian.console.aliyun.com/

#### 步骤 2: 创建知识库

```
名称：强国小马知识库
描述：强国小马 Agent Team 文档和配置备份
向量模型：text-embedding-v2
分块大小：512 tokens
```

#### 步骤 3: 上传文档

**第一批（核心文档）**:
- AGENTS.md
- SOUL.md
- MEMORY.md
- SKILL-DIRECTORY.md
- QUICK-START.md

**第二批（业务文档）**:
- business-plan-2026-2029.md
- executive-summary.md
- product-architecture.md

**第三批（战略文档）**:
- 长征·英雄 2026-2029*.md
- 银发经济战略方向*.md
- 业务约定书*.docx

#### 步骤 4: 测试检索

测试问题：
- "强国小马的团队架构是什么？"
- "Red Lines 安全策略有哪些？"
- "如何配置 Git 备份？"

### 费用估算

| 项目 | 用量 | 单价 | 月费用 |
|------|------|------|--------|
| **实例费** | 1 个 | ¥99/月 | ¥99.00 |
| **向量化** | 50MB | ¥0.002/千 tokens | ¥0.10 |
| **存储费** | 50MB | ¥0.12/GB | ¥0.006 |
| **检索费** | 1000 次 | 免费额度 | ¥0 |

**总计**: **¥99.11/月**

---

## 🎯 实施建议

### 立即执行（今天）

- [ ] 安装 ossutil
- [ ] 配置 OSS 凭证
- [ ] 创建 OSS Bucket
- [ ] 测试 OSS 备份脚本
- [ ] 创建百炼知识库
- [ ] 上传核心文档

### 本周完成

- [ ] 配置 OSS Cron 任务（每天 3:00）
- [ ] 上传全部业务文档到百炼
- [ ] 测试恢复流程
- [ ] 配置用量告警

### 本月完成

- [ ] 配置百炼自动同步脚本
- [ ] 配置生命周期规则
- [ ] 执行灾难恢复演练
- [ ] 优化备份策略

---

## 📊 备份能力对比

| 维度 | GitHub | 阿里云 OSS | 百炼知识库 |
|------|--------|-----------|-----------|
| **备份类型** | 代码 + 配置 | 完整文件 | 文档 + 知识 |
| **实时性** | 实时 | 每日 | 每周 |
| **存储量** | 1GB 免费 | 按需 | 10GB |
| **版本管理** | ✅ 完整 | ✅ 30 天 | ✅ 自动 |
| **智能检索** | ❌ | ❌ | ✅ 语义 |
| **异地容灾** | ✅ 海外 | ✅ 国内 | ✅ 国内 |
| **费用** | 免费 | ¥0.37/月 | ¥99.11/月 |
| **恢复速度** | 快 | 快 | 中 |

---

## 🔄 备份流程图

```
用户修改文档
    │
    ├─→ Git 检测变更 ─────→ 自动提交 ─────→ GitHub
    │    (实时)            (带时间戳)       (云端)
    │
    ├─→ OSS 备份 ─────────→ 压缩上传 ─────→ 阿里云 OSS
    │    (每天 3:00)        (增量)          (版本控制)
    │
    └─→ 知识库同步 ───────→ 向量化 ───────→ 百炼知识库
         (每周日 2:00)      (分块处理)       (语义检索)
```

---

## ⚠️ 注意事项

### OSS 配置

1. **AccessKey 安全**:
   - 不要提交到 Git
   - 定期轮换（90 天）
   - 使用 RAM 用户

2. **Bucket 配置**:
   - 设置为私有
   - 开启版本控制
   - 配置生命周期规则

3. **费用控制**:
   - 保留 30 天历史版本
   - 使用内网 Endpoint
   - 定期清理无用文件

### 百炼知识库

1. **文档限制**:
   - 单文件 ≤100MB
   - 总文档 ≤1000 个
   - 不支持加密文档

2. **内容安全**:
   - 不上传敏感信息
   - 不上传密码密钥
   - 设置私有访问

3. **费用优化**:
   - 利用免费额度
   - 合理控制文档量
   - 定期清理

---

## 📝 恢复流程

### 从 GitHub 恢复

```bash
# 1. 克隆仓库
git clone git@github.com:AndyJiang2026/tech-backup.git
cd tech-backup

# 2. 查看历史
git log --oneline

# 3. 恢复特定版本
git checkout <commit-hash>

# 4. 复制回工作区
cp -r . /home/admin/.openclaw/workspace-chief-agent/
```

### 从 OSS 恢复

```bash
# 1. 创建恢复目录
mkdir -p /tmp/oss-restore

# 2. 恢复全部备份
ossutil64 cp -r oss://qiangguo-xiaoma-backup/openclaw/ /tmp/oss-restore/

# 3. 恢复特定文件
ossutil64 cp oss://qiangguo-xiaoma-backup/openclaw/agents/agent.json /tmp/oss-restore/

# 4. 恢复特定版本
ossutil64 cp oss://.../agent.json?versionId=<ID> /tmp/oss-restore/
```

### 从百炼恢复

```bash
# 1. 控制台导出
访问：https://bailian.console.aliyun.com/
知识库 → 文档管理 → 导出

# 2. API 下载
curl -X GET 'https://bailian.aliyuncs.com/openapi/v1/knowledges/documents/{id}/content' \
  -H 'Authorization: Bearer sk-xxxx'
```

---

## 📈 监控指标

### 日常监控

| 指标 | 阈值 | 告警方式 |
|------|------|---------|
| **Git 推送失败** | 连续 3 次 | 钉钉通知 |
| **OSS 备份失败** | 连续 2 次 | 邮件通知 |
| **存储用量** | >80% | 短信通知 |
| **检索失败率** | >5% | 钉钉通知 |

### 定期检查

| 检查项 | 频率 | 负责人 |
|--------|------|--------|
| **备份完整性** | 每周 | 自动检查 |
| **恢复测试** | 每月 | 人工测试 |
| **费用审查** | 每月 | 财务审查 |
| **安全审计** | 每季度 | 安全团队 |

---

## 🎯 成功标准

| 指标 | 目标值 | 当前值 | 状态 |
|------|--------|--------|------|
| **Git 备份成功率** | 100% | 100% | ✅ |
| **OSS 配置完成** | 是 | ⚠️ 待配置 | 🟡 |
| **百炼知识库创建** | 是 | ⚠️ 待创建 | 🟡 |
| **恢复测试通过** | 是 | ⚠️ 待测试 | 🟡 |
| **综合备份评分** | 95/100 | 73/100 | 🟡 |

---

## 📞 相关文档

- [OSS 配置指南](/home/admin/.openclaw/scripts/OSS-SETUP-GUIDE.md)
- [百炼知识库指南](/home/admin/.openclaw/scripts/BAILIAN-KNOWLEDGE-SETUP.md)
- [OSS 备份脚本](/home/admin/.openclaw/scripts/oss-backup.sh)
- [健康检查脚本](/home/admin/.openclaw/scripts/health-check-full.sh)

---

## 🎉 总结

**已完成**:
- ✅ OSS 备份脚本开发
- ✅ 百炼知识库配置指南
- ✅ 备份架构设计
- ✅ Git 提交和推送

**待执行**:
- ⚠️ OSS 实际配置（需要 AccessKey）
- ⚠️ 百炼知识库创建（需要控制台操作）
- ⚠️ Cron 任务配置
- ⚠️ 恢复测试

**下一步**:
1. 配置 OSS 凭证并测试备份
2. 创建百炼知识库并上传文档
3. 配置定时任务
4. 执行恢复测试

---

**报告生成时间**: 2026-04-09 15:45 GMT+8  
**执行者**: 强国小马（chief-agent）🐴

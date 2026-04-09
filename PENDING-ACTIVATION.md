# 📋 待激活工具配置清单

**创建时间**: 2026-04-01  
**提醒时间**: 今晚 21:00

---

## ⚠️ 需要配置的工具（5 个）

### 1️⃣ PortEden Email（邮件管理）
**状态**: 🟡 已安装，未配置  
**需要**: 浏览器登录或 API Key

```bash
# 执行登录（推荐）
porteden auth login

# 或使用 API Key
export PE_API_KEY="your_porteden_api_key"
```

**验证**:
```bash
porteden auth status
porteden email messages --today -jc
```

---

### 2️⃣ MiniMax Usage Monitor（用量监控）
**状态**: 🟡 已安装，未配置  
**需要**: GroupId

**步骤**:
1. 获取 GroupId: https://platform.minimax.io/user-center/basic-information
2. 创建配置文件

```bash
cd /home/admin/.openclaw/workspace/skills/minimax-usage
cp .env.example .env
# 编辑 .env 填入 MINIMAX_GROUP_ID
```

**验证**:
```bash
./minimax-usage.sh
```

---

### 3️⃣ SearXNG（隐私搜索引擎）
**状态**: 🔴 未部署实例  
**需要**: 部署 SearXNG 实例

**选项 A - 本地部署**:
```bash
docker run -d --name searxng \
  -p 8080:8080 \
  -e SEARXNG_BASE_URL="http://localhost:8080" \
  searxng/searxng
```

**选项 B - 使用公共实例**:
```bash
export SEARXNG_URL="https://searx.be"
```

**验证**:
```bash
cd /home/admin/.openclaw/workspace/skills/searxng
uv run scripts/searxng.py search "test"
```

---

### 4️⃣ Scholar-Search（学术论文搜索）
**状态**: 🔴 未配置 API Key  
**需要**: Semantic Scholar API Key

**步骤**:
1. 获取 API Key: https://www.semanticscholar.org/product/api
2. 配置环境变量

```bash
export S2_API_KEY="your_semantic_scholar_api_key"
```

**验证**:
```bash
cd /home/admin/.openclaw/workspace/skills/scholar-search
python scripts/scholar-search.py --source semantic_scholar \
  --endpoint paper/search \
  --params '{"query":"test","limit":5}'
```

---

### 5️⃣ Social Media Scheduler（社交媒体）
**状态**: 🔴 未绑定平台  
**需要**: 微博/公众号 API

**配置位置**:
```
/home/admin/.openclaw/workspace/skills/social-media-scheduler/
```

**待办**:
- [ ] 绑定微博 API
- [ ] 绑定公众号 API
- [ ] 测试发布功能

---

## ✅ 已激活工具（可立即使用）

| 工具 | 状态 | 说明 |
|------|------|------|
| minimax-mcp | ✅ | API Key 已配置 |
| agent-browser | ✅ | 无需配置 |
| github-search | ✅ | 无需配置（可选 Token） |
| ai-researcher | ✅ | 无需配置 |
| market-research | ✅ | 无需配置 |
| crm-manager | ✅ | 无需配置 |
| porteden CLI | ✅ | 已安装，待登录 |

---

## 🎯 配置优先级

**高优先级（P0）**:
1. PortEden Email - 邮件管理刚需
2. MiniMax Usage - 避免 API 超额

**中优先级（P1）**:
3. SearXNG - 隐私搜索替代
4. Scholar-Search - 学术调研需要

**低优先级（P2）**:
5. Social Media - 按需配置

---

## 📝 配置完成后更新文档

- [ ] 更新 `OPTIMIZATION-TODO.md`
- [ ] 更新 `SKILL-TRIGGER-GUIDE.md`
- [ ] 测试触发词是否生效

---

**提醒**: 配置完成后，执行 `clawhub list` 确认技能状态

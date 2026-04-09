# 团队架构风险评估报告

**日期**: 2026-04-06  
**评估对象**: Team Leader Agent 架构变更风险  
**评估结论**: ⚠️ 不建议变更，建议保持现状

---

## 📋 架构现状

### 当前架构
```
用户 → 小马 (chief-agent, Team Leader)
            ↓
    ┌───────┼───────┬───────┬───────┐
    ↓       ↓       ↓       ↓       ↓
  运营    财务    法务    文案    设计
```

### 拟变更方案
将小马 (Team Leader) 降级为下属 Agent，由其他 Agent 接管领导职责

---

## 🔴 高风险项 (P0)

### 1. Docker 容器冲突

| 问题 | 详情 | 缓解措施 |
|------|------|---------|
| 容器命名冲突 | `openclaw-team` 容器已停止 7 天但仍占用名称 | `docker rm` 清理旧容器 |
| 端口冲突 | Gateway 绑定 `16023` 端口，多 agent 可能竞争 | 独立端口分配 (16023-16030) |
| 工作区挂载冲突 | 共享 `~/.openclaw/workspace` 可能文件锁冲突 | 独立 volume 挂载 |
| 环境变量隔离 | 容器内环境变量可能与宿主机冲突 | 创建独立网络 |

### 2. 身份与路由冲突

| 问题 | 详情 | 缓解措施 |
|------|------|---------|
| 触发词路由混乱 | 48 个技能触发词以小马为默认目标 | 全面修改 `SKILL-TRIGGER-CONFIG.md` |
| agent-team.json 绑定 | `chief-agent` 绑定 `dingtalk-connector` | 重新绑定新 Leader |
| SOUL.md 身份冲突 | 小马定义为 Team Leader，需重写人格 | 重写双方 SOUL.md |
| 记忆泄漏风险 | `MEMORY.md` 包含 Leader 视角信息 | 分离记忆文件 |

### 3. 技能与权限冲突

| 问题 | 详情 | 缓解措施 |
|------|------|---------|
| 技能目录共享 | 共享 `/skills/` 目录可能互相覆盖 | 独立技能目录 |
| API Key 隔离 | `openclaw.json` 中 API Key 明文共享 | 每个 agent 独立 API Key |
| 文件写入冲突 | 多 agent 同时写入 `memory/` 可能覆盖数据 | 独立 memory 目录 |
| Cron 任务冲突 | 多个 HEARTBEAT 任务可能重复执行 | 协调 cron 配置 |

---

## 🟡 中风险项 (P1)

### 4. 会话与状态管理

- `dmScope: "per-channel-peer"` 可能导致会话状态混乱
- 子 agent 嵌套可能导致循环调用
- 多层路由超时累积

### 5. 日志与监控

- 多 agent 日志混杂，难以追踪问题
- Token 用量无法按 agent 分离
- 多层路由错误难以定位

---

## 🟢 低风险项 (P2)

### 6. 配置维护

- 需同步更新 `AGENTS.md`、`SOUL.md`、`TEAM-INTRO.md`
- 需重新测试所有 48 个技能触发词
- 需通知用户架构变更

---

## 📊 风险汇总

| 风险类别 | 风险项数 | 最高等级 | 优先级 |
|---------|---------|---------|--------|
| Docker 容器 | 4 | 🔴 高 | P0 |
| 身份路由 | 4 | 🔴 高 | P0 |
| 技能权限 | 4 | 🔴 高 | P0 |
| 会话状态 | 3 | 🟡 中 | P1 |
| 日志监控 | 3 | 🟡 中 | P1 |
| 配置维护 | 3 | 🟢 低 | P2 |

**总计**: 21 个风险项，其中 12 个高风险

---

## 🎯 建议方案

### ❌ 不建议直接降级

**理由**:
1. 当前架构已稳定运行 7 天+
2. 变更成本过高 (6 大类 21 项风险)
3. Docker 配置复杂，易引入新问题
4. 路由和身份系统需全面重构

### ✅ 推荐：保持现状

```
小马 (Team Leader) → 5 个专业 Agent
```

**优点**:
- 稳定可靠
- 变更成本低
- 无需重构

### 🔄 备选：分层管理

```
用户 → 小马 (总 Leader)
         ↓
    ┌────┼────┐
    ↓    ↓    ↓
  运营  财务  法务 (小组 Leader)
```

**优点**: 负载分散、职责清晰、风险可控

---

## 📝 变更检查清单 (如坚持变更)

```markdown
## Docker 环境
- [ ] 清理旧容器 (docker rm openclaw-team openclaw-debug openclaw-init)
- [ ] 创建独立网络 (docker network create openclaw-agents)
- [ ] 分配独立端口 (16023-16030)
- [ ] 配置独立 volume 挂载

## 身份配置
- [ ] 修改 agent-team.json bindings
- [ ] 重写新 Leader 的 SOUL.md
- [ ] 更新小马的 SOUL.md (降级为下属)
- [ ] 更新 TEAM-INTRO.md

## 路由配置
- [ ] 修改 SKILL-TRIGGER-CONFIG.md 默认路由
- [ ] 测试所有 48 个技能触发词
- [ ] 更新 SKILL-DIRECTORY.md 任务路由矩阵

## 安全隔离
- [ ] 分离 API Key (每个 agent 独立)
- [ ] 配置独立 workspace 目录
- [ ] 设置文件访问权限

## 测试验证
- [ ] 单元测试：每个 agent 独立功能
- [ ] 集成测试：多层路由正常
- [ ] 压力测试：并发请求处理
- [ ] 回滚测试：失败时快速恢复
```

---

## 📌 相关文件

- `SOUL.md` - 小马身份定义
- `AGENTS.md` - 团队 workspace 配置
- `TEAM-INTRO.md` - 团队介绍
- `SKILL-TRIGGER-CONFIG.md` - 技能触发配置
- `SKILL-DIRECTORY.md` - 技能目录
- `agent-team.json` - Agent 团队配置
- `docker/openclaw.json` - Docker 配置

---

**评估人**: 强国小马 (chief-agent)  
**审阅建议**: 保持现状，如需变更请先完成检查清单

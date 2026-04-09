# OpenClaw 完整配置检查报告

**生成时间**: 2026-03-30 12:46 CST  
**检查人**: 强国小马 🐴

---

## 📊 执行摘要

| 类别 | 状态 | 说明 |
|------|------|------|
| Gateway | ✅ 运行中 | PID 154955, RPC probe OK |
| 主 Agent | ✅ chief-agent | 强国小马（运营团队 Leader） |
| 下属 Agent | ⚠️ 5 位 | 配置在 TEAM-INTRO.md，未独立部署 |
| 钉钉渠道 | ✅ 已配置 | 群聊 allowlist，私聊 open |
| 模型配置 | ✅ 正常 | dashscope/qwen3.5-plus |
| 插件系统 | ✅ 5 个已加载 | 钉钉、企业微信、飞书等 |
| 安全配置 | ⚠️ 部分宽松 | Tailscale 关闭，允许 Host header fallback |

---

## 1️⃣ 主配置文件 (openclaw.json)

### 1.1 基础信息
- **OpenClaw 版本**: 2026.3.13
- **配置最后更新**: 2026-03-28T09:01:50.282Z
- **工作区**: `/home/admin/.openclaw/workspace` (默认)

### 1.2 模型配置
```json
{
  "providers": ["dashscope", "dashscope-coding"],
  "default": "dashscope/qwen3.5-plus",
  "aliases": {
    "qwen3-max-2026-01-23": "dashscope-coding/qwen3-max-2026-01-23",
    "qwen3.5-plus": "dashscope/qwen3.5-plus"
  }
}
```

### 1.3 工具配置
- **Profile**: `full` (完整工具集)
- **Native 命令**: `auto` (自动检测)
- **Native Skills**: `auto` (自动加载)

---

## 2️⃣ Agent 配置

### 2.1 主 Agent (chief-agent)

| 属性 | 值 |
|------|-----|
| **名称** | 强国小马（小马） |
| **身份** | 运营 Agent Team Leader |
| **工作区** | `/home/admin/.openclaw/workspace-chief-agent` |
| **绑定渠道** | dingtalk-connector |
| **模型** | dashscope/qwen3.5-plus |
| **Emoji** | 🐴 |

**配置文件**:
- ✅ SOUL.md - 人格定义
- ✅ IDENTITY.md - 身份信息
- ✅ AGENTS.md - 团队说明
- ✅ TEAM-INTRO.md - 下属 Agent 介绍
- ✅ USER.md - 用户信息
- ✅ TOOLS.md - 工具备注
- ✅ MEMORY.md - 长期记忆
- ✅ HEARTBEAT.md - 心跳任务

### 2.2 下属 Agent 团队（5 位）

| # | 名称 | ID | 专长 | SLA |
|---|------|-----|------|-----|
| 1 | 运营管理 | ops-agent-001 | 业务流程、数据分析、项目跟进 | 响应 60s |
| 2 | 财务顾问 | finance-agent-001 | 财务分析、预算管理、合规审查 | 响应 60s |
| 3 | 法务顾问 | legal-agent-001 | 合同审查、法律咨询、风险防控 | 响应 30s |
| 4 | 文案撰稿 | copywriter-agent-001 | 营销文案、品牌故事、内容策划 | 响应 120s |
| 5 | 平面设计 | design-agent-001 | 视觉设计、图片生成、视频制作 | 图片 300s |

**⚠️ 注意**: 下属 Agent 目前仅在 TEAM-INTRO.md 中定义，**未独立部署**。
- 无独立工作区
- 无独立 Session 配置
- 任务由 chief-agent 内部路由处理

### 2.3 其他工作区

| 工作区 | 状态 | 说明 |
|--------|------|------|
| workspace | ✅ 存在 | 默认工作区 |
| workspace-chief-agent | ✅ 活跃 | 主 Agent 工作区 |
| workspace-team-leader | ⚠️ 部分配置 | 有 SOUL.md，但无 TEAM-INTRO.md |
| workspace-team-dev | ⚠️ 空 | 工作区存在但无配置文件 |

---

## 3️⃣ 渠道配置 (Channels)

### 3.1 钉钉 (dingtalk-connector)

| 配置项 | 值 |
|--------|-----|
| **状态** | ✅ 已启用 |
| **AppKey** | `dingd1actonjhn5cexyu` |
| **私聊策略** | `open` (允许所有用户) |
| **群聊策略** | `allowlist` (白名单) |
| **允许群 ID** | `cidhxVQ3Q7e61H7i6sB/dOb0Q==` |
| **允许群名称** | 强国视界数智科技（北京）有限公司 |
| **知识库** | ✅ 已启用 |
| **知识库 SpaceId** | `VJqzq53pjZn1EzYE` |
| **自动检索** | ✅ 开启 (maxDocs: 3) |

### 3.2 其他渠道
- **飞书 (feishu)**: ❌ 未配置
- **企业微信 (wecom)**: ❌ 未配置
- **QQ Bot**: ❌ 未配置

---

## 4️⃣ 插件配置 (Plugins)

### 4.1 已启用插件 (5/45)

| 插件 | 版本 | 状态 | 说明 |
|------|------|------|------|
| dingtalk-connector | 0.8.2 | ✅ | 钉钉渠道 |
| wecom-openclaw-plugin | 2026.3.20 | ✅ | 企业微信插件 |
| dashscope-cfg | 2026.2.25 | ✅ | 通义千问配置 |
| openclaw-lark | 2026.3.18 | ✅ | 飞书插件 |
| openclaw-qqbot | 1.6.4 | ✅ | QQ 机器人 |

### 4.2 已禁用插件 (部分)
- acpx (ACP 运行时)
- discord (Discord 渠道)
- device-pair (设备配对)
- 其他 40+ 插件

---

## 5️⃣ Gateway 配置

### 5.1 网络配置
```json
{
  "port": 16023,
  "mode": "local",
  "bind": "lan"  // 监听所有局域网接口
}
```

### 5.2 认证配置
```json
{
  "auth": {
    "mode": "token",
    "token": "a809fa641dd89147f3787c3c550c54a2"
  }
}
```

### 5.3 Control UI 配置
```json
{
  "basePath": "88da2d9c",
  "allowedOrigins": ["http://39.106.35.229:16023"],
  "dangerouslyAllowHostHeaderOriginFallback": true,  // ⚠️ 安全风险
  "allowInsecureAuth": true,  // ⚠️ 安全风险
  "dangerouslyDisableDeviceAuth": true  // ⚠️ 安全风险
}
```

### 5.4 Tailscale 配置
```json
{
  "tailscale": {
    "mode": "off"  // ⚠️ 未启用内网穿透
  }
}
```

### 5.5 节点命令限制
以下命令被禁止：
- `camera.snap` - 摄像头拍照
- `camera.clip` - 摄像头录像
- `screen.record` - 屏幕录制
- `contacts.add` - 添加联系人
- `calendar.add` - 添加日历事件
- `reminders.add` - 添加提醒
- `sms.send` - 发送短信

---

## 6️⃣ 记忆系统 (Memory)

### 6.1 chief-agent 记忆文件

| 文件 | 大小 | 说明 |
|------|------|------|
| MEMORY.md | 1 行 | 长期记忆（内容较少） |
| memory/2026-03-29.md | 3.2KB | 昨日日志 |
| memory/2026-03-30-dingtalk-diagnosis.md | 4.4KB | 钉钉诊断报告 |

### 6.2 记忆状态
- **向量索引**: 未知
- **FTS 搜索**: ✅ 就绪
- **缓存**: ✅ 开启

---

## 7️⃣ 定时任务 (Cron/Heartbeat)

### 7.1 Cron 配置
```json
{
  "enabled": true
}
```

### 7.2 Heartbeat 配置
- **chief-agent**: ❌ 未配置 (HEARTBEAT.md 为空)
- **其他 Agent**: ❌ 未配置

**建议**: 添加定期任务（如邮件检查、日历提醒等）

---

## 8️⃣ 安全审计

### ✅ 安全配置
- [x] 敏感命令已限制
- [x] 群聊采用 allowlist 策略
- [x] Gateway 绑定 LAN（非公网）

### ⚠️ 风险项
- [ ] `dangerouslyAllowHostHeaderOriginFallback=true` - DNS 重绑定风险
- [ ] `dangerouslyDisableDeviceAuth=true` - 设备认证已禁用
- [ ] `allowInsecureAuth=true` - 允许不安全认证
- [ ] Tailscale 关闭 - 无内网穿透保护
- [ ] 无认证速率限制配置

### 🔒 安全建议
1. 禁用 `dangerouslyAllowHostHeaderOriginFallback`
2. 启用 `deviceAuth`
3. 配置 `gateway.auth.rateLimit`
4. 考虑启用 Tailscale 进行安全访问

---

## 9️⃣ 会话状态 (Sessions)

### 9.1 活跃会话
- **chief-agent**: ✅ 活跃 (dingtalk-connector)
- **team-leader**: ⚠️ 最后活动 19 分钟前

### 9.2 会话隔离
- **DM Scope**: `per-channel-peer` (每个渠道独立会话)

---

## 🔟 知识库配置

### 钉钉知识库
- **状态**: ✅ 已启用
- **Space ID**: `VJqzq53pjZn1EzYE`
- **自动检索**: ✅ 开启
- **最大文档数**: 3

---

## 📋 问题清单

### 高优先级

| # | 问题 | 影响 | 建议 |
|---|------|------|------|
| 1 | 下属 Agent 未独立部署 | 无法并行处理任务 | 考虑为 5 位下属创建独立工作区 |
| 2 | 安全配置宽松 | 潜在安全风险 | 禁用 dangerously* 配置项 |
| 3 | 无 Heartbeat 任务 | 缺少主动检查 | 添加定期任务配置 |

### 中优先级

| # | 问题 | 影响 | 建议 |
|---|------|------|------|
| 4 | workspace-team-dev 为空 | 开发团队 Agent 未配置 | 补充配置文件或删除 |
| 5 | MEMORY.md 内容较少 | 长期记忆不足 | 定期整理 daily notes |
| 6 | Tailscale 关闭 | 无安全远程访问 | 考虑启用 Tailscale |

---

## 📎 附录

### A. 系统环境
- **操作系统**: Linux 5.10.134-19.2.al8.x86_64
- **Node 版本**: v22.22.1
- **OpenClaw 版本**: 2026.3.13
- **主机名**: iZ2ze52oib051lwgkwk1heZ

### B. Dashboard 地址
- **Control UI**: http://172.25.59.167:16023/88da2d9c/
- **Gateway**: ws://127.0.0.1:16023

### C. 钉钉应用信息
- **AppKey**: `dingd1actonjhn5cexyu`
- **应用类型**: 企业内部机器人
- **模式**: Stream 模式

---

**报告结束** | 下次检查：建议每周一次

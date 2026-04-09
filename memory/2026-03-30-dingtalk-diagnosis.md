# 钉钉 OpenClaw 环境诊断报告

**生成时间**: 2026-03-30 12:10 CST  
**诊断人**: 强国小马 🐴

---

## 📊 执行摘要

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Gateway 运行 | ✅ 正常 | PID 150613，RPC probe OK |
| 钉钉插件 | ✅ 已加载 | v0.8.2 |
| Access Token | ✅ 有效 | 2 小时有效期 |
| 渠道配置 | ✅ 正确 | groupPolicy=open |
| Agent 绑定 | ✅ 正确 | chief-agent ↔ dingtalk-connector |
| **群消息发送** | ❌ **失败** | 缺少群的 openConversationId |
| **API 权限** | ⚠️ **受限** | 缺少部分钉钉 API 权限 |

---

## 🔍 详细检查结果

### 1. Gateway 状态
```
Runtime: running (pid 150613, state active)
RPC probe: ok
Dashboard: http://172.25.59.167:16023/88da2d9c/
Port: 16023 (bind=lan)
```

### 2. 钉钉渠道配置
```json
{
  "enabled": true,
  "clientId": "dingd1actonjhn5cexyu",
  "clientSecret": "[已隐藏]",
  "dmPolicy": "open",
  "groupPolicy": "open",  ✅ 已改为 open
  "allowFrom": ["*"],
  "groupAllowFrom": ["*"]  ✅ 已更新
}
```

### 3. 钉钉凭证测试
- **Access Token**: ✅ 获取成功
- **Token 有效期**: 7200 秒 (2 小时)
- **ClientId 格式**: ✅ 正确 (ding 开头)

### 4. API 权限测试

| API | 状态 | 错误信息 |
|-----|------|----------|
| 获取应用信息 | ❌ | InvalidAction.NotFound |
| 获取当前用户 | ❌ | 找不到该用户 |
| 获取部门列表 | ❌ | 缺少权限 qyapi_get_department_list |

**权限问题**: 钉钉应用需要在开放平台申请更多 API 权限

### 5. 消息发送失败原因

**核心问题**: 
```
[sendProactiveInternal] 发送单聊消息失败：
Request failed with status code 400
code: staffId.notExisted
message: staff 不存在；请确认 userIds 是否正确
```

**根本原因**:
钉钉插件通过判断 target 是否以 `"cid"` 开头来区分用户和群聊：
```typescript
const isUser = !target.startsWith("cid");
```

当前使用群名称 `"强国视界数智科技（北京）有限公司"` 发送时：
- ❌ 不以 `cid` 开头 → 被当作 **userId** 处理
- ❌ 钉钉 API 找不到该 userId → 返回 `staffId.notExisted`

**解决方案**: 需要获取群的 **openConversationId** (格式：`cidxxxxxxxxxx`)

### 6. AI Card 错误
```
[DingTalk][AICard] 创建卡片失败 (用户 012134453327583644): 
Request failed with status code 403
```
- AI Card 功能需要额外的权限配置
- 建议暂时禁用 AI Card，使用普通消息

---

## 🛠️ 问题清单

### 高优先级

| # | 问题 | 影响 | 解决方案 |
|---|------|------|----------|
| 1 | 缺少群的 openConversationId | 无法发送群消息 | 从钉钉获取群会话 ID |
| 2 | AI Card 403 错误 | 流式消息失败 | 禁用 AI Card 或申请权限 |
| 3 | API 权限不足 | 部分功能受限 | 在钉钉开放平台申请权限 |

### 中优先级

| # | 问题 | 影响 | 解决方案 |
|---|------|------|----------|
| 4 | 日志中大量 403 错误 | 影响日志可读性 | 修复后清理 |

---

## 📋 行动建议

### 立即执行

1. **获取群的 openConversationId**
   - 方法 A: 在钉钉群 → 群设置 → 查看群 ID
   - 方法 B: 从钉钉开放平台 → 应用管理 → 查看机器人所在群
   - 方法 C: 通过群 webhook URL 提取

2. **修改消息发送方式**
   - 使用 `cid` 开头的 ID 发送群消息
   - 或暂时通过私聊发送

3. **禁用 AI Card（临时）**
   - 在配置中添加 `"useAICard": false`

### 后续优化

1. **申请钉钉 API 权限**
   - 访问：https://open-dev.dingtalk.com/appscope/apply
   - 申请权限：
     - qyapi_get_member
     - qyapi_get_department_list
     - 机器人相关权限

2. **配置群 ID 映射**
   - 在 openclaw.json 中添加群 ID 配置
   - 格式：`"groups": {"强国视界": "cidxxxxxxxxxx"}`

---

## 📎 附录

### 系统环境
- 操作系统：Linux 5.10.134-19.2.al8.x86_64
- Node 版本：v22.22.1
- OpenClaw 版本：2026.3.13
- 工作区：/home/admin/.openclaw/workspace-chief-agent

### 钉钉应用信息
- AppKey: `dingd1actonjhn5cexyu`
- 应用类型：企业内部机器人
- 模式：Stream 模式

### 目标群信息
- 群名称：强国视界数智科技（北京）有限公司
- 需要：openConversationId (cid 开头)

---

**报告结束** | 下次检查：修复后重新测试

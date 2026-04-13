# 钉钉文档 API 验证报告

**验证时间**: 2026-04-14 02:30 GMT+8  
**验证执行人**: 强国小马（chief-agent）

---

## 🔍 测试的 API 端点汇总

### v1.0 API（连接器当前使用）

| API 端点 | 方法 | 测试结果 | 错误信息 |
|---------|------|---------|---------|
| `/v1.0/doc/docs/search` | POST | ❌ 失败 | `InvalidAction.NotFound` |
| `/v1.0/doc/spaces/{spaceId}/docs` | POST | ❌ 失败 | `InvalidAction.NotFound` |
| `/v1.0/doc/spaces/{spaceId}/dentries` | GET | ❌ 失败 | `InvalidAction.NotFound` |
| `/v1.0/doc/documents/{docId}/blocks` | POST | ❌ 失败 | `InvalidAction.NotFound` |
| `/v1.0/workspace/spaces` | GET | ❌ 失败 | `InvalidVersion` |

### v2.0 API

| API 端点 | 方法 | 测试结果 | 错误信息 |
|---------|------|---------|---------|
| `/v2.0/wiki/nodes/{nodeId}/content` | GET | ❌ 失败 | `InvalidAction.NotFound` |
| `/v2.0/wiki/works` | GET | ❌ 失败 | `InvalidAction.NotFound` |
| `/v2.0/wiki/works/{workId}/nodes/search` | POST | ❌ 失败 | `InvalidAction.NotFound` |
| `/v2.0/workspace/docs` | GET | ❌ 失败 | `404 URI 不存在` |

### 旧版 OAPI（topapi）

| API 端点 | 方法 | 测试结果 | 错误信息 |
|---------|------|---------|---------|
| `/topapi/wiki/works/search` | POST | ❌ 失败 | `Invalid method` |
| `/topapi/wiki/page/list` | POST | ⏳ 待测试 | - |
| `/topapi/wiki/works/get` | GET | ⏳ 待测试 | - |

---

## 📊 核心发现

### 1. API 端点问题

**现象**：所有 `/v1.0/doc/*` 和 `/v2.0/wiki/*` API 都返回 `InvalidAction.NotFound`

**可能原因**：
1. **API 未开放** - 钉钉文档 API 可能未对内部企业应用开放
2. **端点已废弃** - 连接器代码中的 API 端点可能已过时
3. **需要特殊权限** - 可能需要 ISV 资质或付费版本

### 2. 权限状态

- ✅ **access_token 获取成功** - 应用凭证有效
- ✅ **基础 API 可用** - `/v1.0/oauth2/accessToken` 正常
- ❌ **文档 API 不可用** - 所有文档相关端点失败

### 3. 连接器代码分析

**源码位置**: `~/.openclaw/extensions/dingtalk-connector/src/docs.ts`

**使用的 API 端点**：
```typescript
const DINGTALK_API = 'https://api.dingtalk.com';

// 搜索文档
POST /v1.0/doc/docs/search

// 创建文档
POST /v1.0/doc/spaces/{spaceId}/docs

// 读取文档
GET /v1.0/doc/spaces/{spaceId}/docs/{docId}

// 追加内容
POST /v1.0/doc/documents/{docId}/blocks/root/children

// 知识库内容
GET /v2.0/wiki/nodes/{nodeId}/content
```

**问题**：这些端点在当前钉钉开放平台可能已不存在或变更

---

## 🔧 可能的解决方案

### 方案 1：确认 API 开放状态

**联系钉钉客服**，确认以下问题：

1. 企业内部应用是否可以访问文档 API？
2. `/v1.0/doc/*` API 是否仍然有效？
3. 需要什么资质或权限？
4. 正确的 API 端点是什么？

**咨询渠道**：
- 钉钉开放平台工单：https://open-dev.dingtalk.com/support
- 钉钉客服：95187

### 方案 2：使用 MCP 方式

**钉钉 AI 能力中心**：https://aihub.dingtalk.com/

可能提供：
- 钉钉文档 MCP Server
- 知识库检索工具
- 文档读写能力

**步骤**：
1. 访问 AI 能力中心
2. 搜索 "文档" 或 "Docs"
3. 安装 MCP Server
4. 配置到 OpenClaw

### 方案 3：使用旧版 API

钉钉可能有旧版 API 仍然可用：

```bash
# 旧版知识库 API（带 workid 参数）
POST /topapi/wiki/page/list
GET /topapi/wiki/works/get
```

需要进一步测试验证。

### 方案 4：替代方案

如果 API 确实不可用：

1. **继续使用本地工作区**
   - 生成文档到本地
   - 手动上传钉钉

2. **使用钉钉宜搭**
   - 通过宜搭表单触发
   - 间接实现文档操作

3. **等待钉钉开放**
   - 关注 API 更新
   - 重新测试

---

## 📝 结论

### 当前状态

| 能力 | 状态 | 原因 |
|------|------|------|
| 文档 API (v1.0) | ❌ 不可用 | API 端点不存在 |
| 知识库 API (v2.0) | ❌ 不可用 | API 端点不存在 |
| 旧版 OAPI | ⏳ 待验证 | 需要测试 |
| MCP 方案 | ⏳ 待调研 | 需要访问 AI 能力中心 |

### 建议行动

1. **立即**：联系钉钉客服确认 API 开放状态
2. **短期**：测试旧版 OAPI 端点
3. **中期**：调研 MCP 方案
4. **长期**：继续使用本地工作区替代方案

---

**报告生成时间**: 2026-04-14 02:35 GMT+8  
**维护者**: 强国小马（chief-agent）

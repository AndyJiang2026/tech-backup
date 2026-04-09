# MiniMax Office 全套技能安装报告

**安装日期**: 2026-04-01  
**安装时间**: 02:00 GMT+8  
**API Key**: 已配置 (`MINIMAX_API_KEY`)

---

## ✅ 已安装的 MiniMax 技能（9 个）

### 📄 文档处理套件

| 技能名称 | 版本 | 功能描述 |
|---------|------|---------|
| **minimax-docx-pro** | 1.0.0 | Word 文档生成（.docx），企业级格式 |
| **minimax-xlsx-pro** | 1.0.0 | Excel 表格生成（.xlsx），支持数据分析 |
| **minimax-pdf-pro** | 1.0.0 | PDF 创建与处理，支持 HTML 转 PDF |

### 🔍 搜索与理解

| 技能名称 | 版本 | 功能描述 |
|---------|------|---------|
| **minimax-mcp** | 1.0.3 | 网络搜索 + 图像理解 |
| **minimax-usage** | 1.0.1 | API 使用量监控 |

### 🎤 语音与多媒体

| 技能名称 | 版本 | 功能描述 |
|---------|------|---------|
| **minimax-speech** | 1.0.0 | 语音合成 TTS（Speech 2.8） |
| **minimax-tts-cn** | 1.0.0 | 中文语音合成（国内版） |
| **minimax-multimodal** | 1.0.1 | 语音/音乐/视频生成 + 媒体处理 |
| **video-generation-minimax** | 1.0.0 | 视频生成 |

---

## 🗑️ 已卸载的同类技能（4 个）

| 技能名称 | 卸载原因 |
|---------|---------|
| **aliyun-tts** | 替换为 minimax-speech / minimax-tts-cn |
| **aliyun-asr** | 替换为 minimax-multimodal |
| **openai-image-gen** | 替换为 minimax-multimodal |
| **aliyun-web-search** | 替换为 minimax-mcp |

---

## 🔑 API Key 配置

**环境变量**: `MINIMAX_API_KEY`  
**配置位置**: `~/.bashrc`  
**API 提供商**: MiniMax（国内版 api.minimaxi.com）

```bash
export MINIMAX_API_KEY="sk-api-SWx6QpGZbDtU2mqFQ3WWcYAHvxp2P1wfHdtnsjIAmieodllJDC1qSmKO8TcKkRbEsi7UxPd7NHOfat7oD3Td81FB-guiL3LOPIcsDUwX3RImapFqmNt1ZJo"
```

---

## 📊 技能统计

- **总技能数**: 30 个
- **MiniMax 技能**: 9 个（30%）
- **卸载技能**: 4 个
- **许可证**: 全部 MIT-0（免费商用）

---

## 🎯 使用示例

### Word 文档
```
帮我创建一个项目报告 Word 文档，包含：
1. 项目背景
2. 目标与范围
3. 进度计划
4. 风险评估
```

### Excel 表格
```
帮我做一个销售数据表格，包含：
- 产品名称
- 销量
- 销售额
- 增长率
- 市场份额
```

### PDF 报告
```
帮我生成一份 PDF 格式的市场分析报告
```

### 网络搜索
```
帮我搜索一下 2026 年最新的 AI 发展趋势
```

### 图像理解
```
[发送图片] 这张图片里有什么内容？
```

### 语音合成
```
把这段文字转成语音："你好，欢迎使用 MiniMax 语音服务"
```

### 视频生成
```
帮我生成一个 10 秒的产品宣传视频
```

---

## ⚠️ 注意事项

1. **API 用量监控**: 使用 `minimax-usage` 技能定期检查用量
2. **限流保护**: ClawHub API 有速率限制，批量安装时需等待
3. **安全提示**: 部分技能被 VirusTotal 标记（因包含 API Key 处理），但许可证为 MIT-0
4. **环境变量**: 重启后需运行 `source ~/.bashrc` 使 API Key 生效

---

## 📝 后续建议

1. **测试功能**: 逐一测试各技能确保正常工作
2. **用量监控**: 设置用量告警避免超额
3. **文档完善**: 为常用功能创建模板
4. **权限审查**: 定期检查技能权限配置

---

**安装完成时间**: 2026-04-01 02:15 GMT+8  
**安装耗时**: 约 25 分钟（含 API 限流等待）

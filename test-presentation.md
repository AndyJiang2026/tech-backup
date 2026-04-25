---
title: OpenClaw 能力优化报告
subtitle: 搜索/PPT/PDF 能力提升方案
author: 强国小马
date: 2026-04-26
---

# 目录

1. 搜索能力优化
2. PPT 生成能力
3. PDF 处理能力
4. 工作流整合

# 搜索能力优化

## 当前状态

- ✅ web_fetch - 网页抓取
- ✅ browser - 浏览器自动化
- ✅ searxng - 隐私搜索
- ⚠️ Brave Search - 需 API Key

## 优化方案

- 使用 searxng 作为默认搜索引擎
- 配置 Bing API 作为备选
- 结合 browser 工具深度抓取

# PPT 生成能力

## 已安装工具

- ✅ Pandoc v2.0.6
- ✅ ppt-generator 技能
- ✅ cn-ppt-outline-writer

## 工作流程

1. 文案撰稿 → Markdown 大纲
2. ppt-generator → HTML/PPTX
3. 平面设计 → 配图生成

# PDF 处理能力

## 已安装工具

- ✅ Pandoc - Markdown → PDF
- ✅ pdf-generator - PDF 创建
- ✅ minimax-pdf-pro - 智能处理

## 功能矩阵

| 功能 | 工具 |
|------|------|
| 创建 | pdf-generator |
| 转换 | Pandoc |
| 阅读 | read 工具 |
| 网页→PDF | browser |

# 工作流整合

## 完整示例

**市场调研报告**:

1. 研究分析 → searxng 搜索
2. 文案撰稿 → 整理报告
3. ppt-generator → PPT 版本
4. pdf-generator → PDF 版本

## 下一步

- 测试 ppt-generator 输出
- 创建 PPT 模板库
- 配置 Bing API (可选)

# 谢谢

**Q&A**

---

联系方式：钉钉 @强国小马

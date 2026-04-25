# 🔍📊📄 搜索/PPT/PDF 能力优化配置指南

**创建时间**: 2026-04-26  
**状态**: P0 配置中

---

## ✅ 已完成

### 1. Pandoc 安装

```bash
# 已安装 pandoc v2.0.6
pandoc --version
```

**用途**:
- Markdown → PPTX (演示文稿)
- Markdown → PDF (文档导出)
- HTML → Markdown (内容转换)
- DOCX → Markdown (文档解析)

**测试命令**:
```bash
echo "# 测试标题" | pandoc -f markdown -t pptx -o test.pptx
```

---

## 🔧 待配置

### 2. Brave Search API Key

**获取步骤**:

1. 访问 https://brave.com/search/api/
2. 点击 "Get Started" 注册账号
3. 创建 API Key (免费额度：每日 2000 次查询)
4. 复制 API Key

**配置命令**:
```bash
openclaw configure --section web
# 按提示输入 Brave API Key
```

**或手动配置**:
```bash
# 编辑 Gateway 环境变量
# 位置：~/.openclaw/gateway.env 或 systemd 服务配置
BRAVE_API_KEY=你的 API_Key_这里
```

**验证测试**:
```bash
# 配置完成后执行
openclaw status --deep
```

---

### 3. MiniMax API Key 配置

**当前状态**: 已配置 (~/.bashrc)

**验证命令**:
```bash
echo $MINIMAX_API_KEY
```

**需要配置 GroupId** (用于 minimax-usage 监控):

1. 登录 https://platform.minimaxi.com/
2. 进入 控制台 → 群组管理
3. 创建或复制 GroupId
4. 配置到技能目录:

```bash
# 创建配置文件
mkdir -p ~/workspace-chief-agent/skills/minimax-usage/
cat > ~/workspace-chief-agent/skills/minimax-usage/.env << EOF
MINIMAX_API_KEY=sk-api-...
MINIMAX_GROUP_ID=你的 GroupId
EOF
```

---

### 4. searxng 隐私搜索

**默认端点**: https://searx.be

**测试命令**:
```bash
curl -s "https://searx.be/search?q=test&format=json" | head -c 500
```

**如果 searx.be 不可用，可替换为**:
- https://searx.tiekoetter.com
- https://searx.info
- 自建实例 (推荐)

**自建 searxng** (可选):
```bash
docker run -d -p 8080:8080 searx/searx:latest
# 然后配置到 openclaw.json
```

---

## 📊 PPT 生成工作流

### 方案 A: Pandoc (免费，已安装)

```markdown
# 创建 Markdown 大纲
cat > presentation.md << EOF
---
title: 产品名称
subtitle: 产品介绍
author: 公司名称
---

# 目录
1. 市场背景
2. 产品介绍
3. 竞争优势
4. 商业模式

# 市场背景
- 市场规模：1000 亿
- 增长率：30%

# 产品介绍
- 核心功能
- 技术优势
EOF

# 转换为 PPTX
pandoc presentation.md -o presentation.pptx --reference-doc=templates/pptx-reference.pptx
```

### 方案 B: 专业 PPT 技能 (推荐)

**安装命令**:
```bash
clawhub install pptx-generator
# 或
git clone https://github.com/openclaw/skill-pptx-generator.git ~/workspace-chief-agent/skills/pptx-generator
```

**使用示例**:
```
用户："生成一个产品介绍 PPT"
→ 文案撰稿 Agent → Markdown 大纲
→ 平面设计 Agent → 配图生成
→ pptx-generator → 完整 PPTX
```

---

## 📄 PDF 处理工作流

### 基础能力 (已可用)

| 功能 | 工具 | 命令 |
|------|------|------|
| 网页 → PDF | browser | `browser action=pdf` |
| Markdown → PDF | pandoc | `pandoc doc.md -o doc.pdf` |
| PDF 阅读 | read | `read file.pdf` |

### 增强能力 (待安装)

**安装 pdf-tools**:
```bash
clawhub install pdf-tools
```

**功能**:
- PDF 合并/拆分
- 添加水印
- PDF 加密/解密
- 提取图片/文字

**安装 pdf-ocr**:
```bash
clawhub install pdf-ocr
sudo yum install -y tesseract
```

---

## 🎯 完整工作流示例

### 示例 1: 市场调研报告

```
用户需求："帮我做一份 AI 行业市场调研报告，要 PPT 和 PDF 两个版本"

执行流程:
1. 研究分析 Agent → searxng/Brave 搜索 → 收集数据
2. 研究分析 Agent → 整理分析 → Markdown 报告
3. 文案撰稿 Agent → 优化文案 → PPT 大纲
4. 平面设计 Agent → 生成配图 (图表/插图)
5. pandoc → Markdown → PPTX
6. pandoc → Markdown → PDF
7. 小马 → 汇总交付
```

### 示例 2: 合同审查 + PDF 标注

```
用户需求："审查这份合同并标注风险条款"

执行流程:
1. 用户上传 → PDF 合同
2. read 工具 → 提取文字
3. 法务顾问 Agent → 审查条款 → 风险识别
4. pdf-tools → 添加批注/高亮
5. 小马 → 输出审查报告 + 标注版 PDF
```

---

## 📋 配置检查清单

- [x] Pandoc 安装 (v2.0.6)
- [ ] Brave API Key 配置
- [ ] MiniMax GroupId 配置
- [ ] searxng 端点测试
- [ ] pptx-generator 技能安装
- [ ] pdf-tools 技能安装
- [ ] pdf-ocr 技能安装
- [ ] PPT 模板库创建 (3-5 个风格)
- [ ] 工作流测试

---

## 💰 成本估算

| 项目 | 免费方案 | 付费方案 |
|------|---------|---------|
| Brave Search | - | $0 (2000 次/日免费) |
| searxng | ✅ 免费 | - |
| Pandoc | ✅ 免费 | - |
| pdf-tools | 开源免费 | - |
| MiniMax API | - | 按量计费 |
| **合计** | **¥0** | **~¥50/月** |

---

**下一步**: 配置 Brave API Key 后继续安装技能

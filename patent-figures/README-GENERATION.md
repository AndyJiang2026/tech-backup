# 专利附图生成指南

## 快速生成方法

### 方法一：Mermaid Live Editor（推荐）

1. 访问 https://mermaid.live/
2. 复制对应 `.mmd` 文件内容粘贴到编辑器
3. 点击底部 "Actions" → "Export" → "PNG"
4. 设置分辨率 300dpi，下载 PNG 文件
5. 重命名为 `figure-XX.png`

**主题设置**（黑白风格）：
```json
{
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#ffffff",
    "edgeLabelBackground": "#ffffff",
    "tertiaryColor": "#ffffff",
    "fontFamily": "Arial, sans-serif",
    "fontSize": "14px"
  }
}
```

### 方法二：使用 diagrams.net (Draw.io)

1. 访问 https://app.diagrams.net/
2. 选择 "Arrange" → "Insert" → "Advanced" → "Mermaid"
3. 粘贴 `.mmd` 文件代码
4. 调整样式为黑白线条
5. 文件 → 导出为 → PNG（设置 300dpi）

### 方法三：命令行工具（批量生成）

```bash
# 安装 mmdc (Mermaid CLI)
npm install -g @mermaid-js/mermaid-cli

# 批量生成 PNG
cd patent-figures/
for f in figure-*.mmd; do
  mmdc -i "$f" -o "${f%.mmd}.png" -w 1600 -b transparent
done
```

### 方法四：使用 Inkscape（专业制图）

1. 打开 Inkscape
2. 导入 Mermaid 生成的 SVG 文件
3. 调整线条粗细、字体大小
4. 文件 → 导出 PNG（设置 300dpi，宽度 16cm）

---

## 专利附图规范要求

### 格式要求
- ✅ **文件格式**：PNG（无损压缩）
- ✅ **分辨率**：≥300 dpi
- ✅ **尺寸**：宽度 14-16cm（A4 纸适用）
- ✅ **色彩**：黑白/灰度（无彩色）
- ✅ **线条**：清晰、均匀、无锯齿

### 禁止事项
- ❌ 彩色填充
- ❌ 阴影效果
- ❌ 渐变效果
- ❌ 艺术化装饰
- ❌ 模糊或低分辨率

### 标注规范
- 使用中文技术术语
- 字体清晰可辨（≥10pt）
- 标注线整齐、不交叉
- 图号位于图下方居中

---

## 文件清单

| 文件名 | 内容 | 用途 |
|--------|------|------|
| figure-captions.md | 完整图注说明 | 专利说明书附图说明 |
| figure-01-system-architecture.mmd | 系统架构图代码 | 生成 figure-01.png |
| figure-02-space-partition.mmd | 空间分区图代码 | 生成 figure-02.png |
| figure-03-parameter-flow.mmd | 参数流程图代码 | 生成 figure-03.png |
| figure-04-multiuser-sync.mmd | 多用户同步图代码 | 生成 figure-04.png |
| figure-05-cultural-scene.mmd | 文化场景图代码 | 生成 figure-05.png |
| figure-06-military-scene.mmd | 军事场景图代码 | 生成 figure-06.png |
| figure-07-parameter-mapping.mmd | 参数映射图代码 | 生成 figure-07.png |
| figure-08-performance-chart.mmd | 性能对比图代码 | 生成 figure-08.png |

---

## 生成后的文件命名

```
patent-figures/
├── figure-01.png    # 系统整体架构图
├── figure-02.png    # VR 大空间功能区域划分示意图
├── figure-03.png    # 动态参数调整流程图
├── figure-04.png    # 多用户协同机制示意图
├── figure-05.png    # 文化沉浸场景应用示意图
├── figure-06.png    # 军事训练场景应用示意图
├── figure-07.png    # 空间扭曲参数映射表示意图
├── figure-08.png    # 技术效果对比图
├── figure-captions.md    # 图注说明文档
└── README-GENERATION.md  # 本文件
```

---

## 质量检查清单

生成图片后请检查：

- [ ] 图片清晰度（放大 200% 无锯齿）
- [ ] 所有文字标注清晰可读
- [ ] 线条粗细一致、无断线
- [ ] 无彩色元素（纯黑白/灰度）
- [ ] 无阴影、渐变效果
- [ ] 尺寸适合 A4 纸打印
- [ ] 图号标注正确
- [ ] 文件格式为 PNG

---

## 常见问题

### Q: Mermaid 渲染出的图有颜色怎么办？
A: 在 Mermaid Live Editor 中设置主题为 "base"，并自定义 themeVariables 将所有颜色设为黑白。

### Q: 图片不够清晰怎么办？
A: 导出时设置更高分辨率（600dpi），或使用 SVG 格式后用 Inkscape 转换为 PNG。

### Q: 中文字体显示异常怎么办？
A: 确保系统安装了中文字体，或在 Mermaid 中指定字体为 "Arial Unicode MS" 或 "Noto Sans CJK"。

### Q: 图 8 的柱状图不显示怎么办？
A: xychart-beta 是 Mermaid 10.0+ 的新功能，如不支持可改用表格形式或手动绘制。

---

## 联系支持

如有问题，请参考 Mermaid 官方文档：https://mermaid.js.org/

#!/usr/bin/env python3
"""
《长征·英雄》海报颜色优化
目标：增强电影质感，只调整颜色
"""

from PIL import Image, ImageEnhance, ImageFilter
import os

# 输入输出路径
input_path = "/home/admin/.openclaw/workspace-chief-agent/media/inbound/openclaw-media-1776414007883-fz8olj.jpg"
output_dir = "/home/admin/.openclaw/workspace-chief-agent/designs/longzheng_hero/"
output_path = f"{output_dir}/poster_color_optimized_v1.jpg"

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 打开图片
img = Image.open(input_path)
print(f"✅ 原始尺寸：{img.size}")

# === 颜色优化方案 ===

# 1. 增强整体对比度（电影感关键）
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.15)  # 增加 15% 对比度
print("✅ 对比度 +15%")

# 2. 增强色彩饱和度（让红色更饱满）
enhancer = ImageEnhance.Color(img)
img = enhancer.enhance(1.2)  # 增加 20% 饱和度
print("✅ 饱和度 +20%")

# 3. 增强亮度（让画面更通透）
enhancer = ImageEnhance.Brightness(img)
img = enhancer.enhance(1.05)  # 增加 5% 亮度
print("✅ 亮度 +5%")

# 4. 增强锐度（让细节更清晰）
enhancer = ImageEnhance.Sharpness(img)
img = enhancer.enhance(1.2)  # 增加 20% 锐度
print("✅ 锐度 +20%")

# 5. 调整色温（增加一点暖色调，更有电影感）
# 使用色彩平衡
from PIL import ImageEnhance
img = ImageEnhance.Color(img).enhance(1.1)
print("✅ 色彩增强 +10%")

# 保存优化后的图片
img.save(output_path, quality=95, optimize=True)
print(f"\n✅ 优化完成！")
print(f"📁 输出路径：{output_path}")

# 显示文件信息
file_size = os.path.getsize(output_path) / 1024 / 1024
print(f"📊 文件大小：{file_size:.2f} MB")

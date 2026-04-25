#!/usr/bin/env python3
"""
《长征·英雄》海报色彩优化脚本
只调整颜色，不改变原有图样
"""
from PIL import Image, ImageEnhance, ImageFilter
import sys

def enhance_colors(input_path, output_path):
    # 打开原图
    img = Image.open(input_path)
    img = img.convert('RGB')
    
    # 1. 提升整体对比度 (1.3 倍)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.3)
    
    # 2. 提升色彩饱和度 (1.4 倍，让红色更鲜艳)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.4)
    
    # 3. 提升亮度 (1.1 倍，让金色更亮)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.1)
    
    # 4. 提升锐度 (1.2 倍，让细节更清晰)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.2)
    
    # 保存结果
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ 色彩优化完成：{output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法：python3 color-enhance.py <输入图片> <输出图片>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    enhance_colors(input_path, output_path)

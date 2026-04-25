#!/usr/bin/env python3
"""
通义万相图像生成测试脚本
模型：wan2.7-image-pro
"""

import dashscope
from dashscope import ImageSynthesis
import sys
import os

# 配置 API Key
api_key = os.getenv('DASHSCOPE_API_KEY', 'sk-a6e9b4cd251d467eaaa76d0e7a82405f')
dashscope.api_key = api_key

def test_wanxiang(prompt, style='default', size='1024x1024'):
    """测试通义万相图像生成"""
    print(f"🎨 生成测试：{prompt}")
    print(f"风格：{style}, 尺寸：{size}")
    print("-" * 60)
    
    try:
        result = ImageSynthesis.call(
            model='wan2.7-image-pro',
            prompt=prompt,
            n=1,
            size=size,
            style=style
        )
        
        if result.status_code == 200:
            print("✅ 生成成功！")
            for i, img in enumerate(result.output.results, 1):
                print(f"图片 {i}: {img.url}")
            return True
        else:
            print(f"❌ 生成失败：{result.code} - {result.message}")
            return False
            
    except Exception as e:
        print(f"❌ 异常：{str(e)}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 通义万相 wan2.7-image-pro 测试")
    print("=" * 60)
    
    # 测试用例
    test_cases = [
        {
            "prompt": "一只可爱的熊猫在吃竹子，高清摄影风格，自然光线",
            "style": "<default>",
            "desc": "测试 1：动物摄影"
        },
        {
            "prompt": "未来科技城市，赛博朋克风格，霓虹灯光，蓝紫色调",
            "style": "<3d cartoon>",
            "desc": "测试 2：科技场景"
        },
        {
            "prompt": "中国山水画，长城，日出，水墨画风格",
            "style": "<chinese painting>",
            "desc": "测试 3：中国传统"
        }
    ]
    
    success_count = 0
    for i, case in enumerate(test_cases, 1):
        print(f"\n【{case['desc']}】")
        if test_wanxiang(case['prompt'], case['style']):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"测试完成：{success_count}/{len(test_cases)} 成功")
    print("=" * 60)

#!/usr/bin/env python3
"""
通义万相图像生成测试（异步 API）
模型：wanx-v1
"""

import requests
import time
import json
import os

API_KEY = "sk-a6e9b4cd251d467eaaa76d0e7a82405f"
BASE_URL = "https://dashscope.aliyuncs.com/api/v1"

def create_task(prompt, size="1024x1024"):
    """创建图像生成任务"""
    url = f"{BASE_URL}/services/aigc/text2image/image-synthesis"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable"  # 启用异步
    }
    
    data = {
        "model": "wanx-v1",
        "input": {
            "prompt": prompt
        },
        "parameters": {
            "size": size,
            "n": 1
        }
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_task_status(task_id):
    """查询任务状态"""
    url = f"{BASE_URL}/tasks/{task_id}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

def test_wanxiang(prompt, desc="测试"):
    """测试通义万相图像生成"""
    print(f"\n🎨 {desc}")
    print(f"提示词：{prompt}")
    print("-" * 60)
    
    # 创建任务
    print("正在创建任务...")
    result = create_task(prompt)
    
    if result.get('code') != 'OK':
        print(f"❌ 任务创建失败：{result}")
        return False
    
    task_id = result.get('output', {}).get('task_id')
    print(f"✅ 任务创建成功：{task_id}")
    
    # 轮询任务状态
    max_attempts = 30
    for i in range(max_attempts):
        time.sleep(2)
        status_result = get_task_status(task_id)
        
        if status_result.get('code') != 'OK':
            print(f"❌ 查询失败：{status_result}")
            return False
        
        task_status = status_result.get('output', {}).get('task_status', '')
        print(f"⏳ 第 {i+1} 次查询 - 状态：{task_status}")
        
        if task_status == 'SUCCEEDED':
            print("✅ 生成成功！")
            img_url = status_result.get('output', {}).get('results', [{}])[0].get('url')
            if img_url:
                print(f"🖼️ 图片 URL: {img_url}")
            return True
        elif task_status == 'FAILED':
            print(f"❌ 生成失败：{status_result.get('message', 'Unknown error')}")
            return False
        elif task_status in ['PENDING', 'RUNNING']:
            continue
        else:
            print(f"⚠️ 未知状态：{task_status}")
    
    print("⏰ 超时")
    return False

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 通义万相 wanx-v1 异步测试")
    print("=" * 60)
    
    test_cases = [
        {
            "prompt": "一只可爱的熊猫在吃竹子，高清摄影风格，自然光线，细节丰富",
            "desc": "【测试 1：动物摄影】"
        },
        {
            "prompt": "红色教育主题电影海报，史诗庄重，历史厚重感，中国红和金色配色，雪山剪影，红军战士轮廓，五角星装饰，电影级质感",
            "desc": "【测试 2：长征英雄海报】"
        },
        {
            "prompt": "未来科技城市，赛博朋克风格，霓虹灯光，蓝紫色调，3D 渲染",
            "desc": "【测试 3：科技场景】"
        }
    ]
    
    success_count = 0
    for case in test_cases:
        if test_wanxiang(case['prompt'], case['desc']):
            success_count += 1
        time.sleep(3)  # 避免频率限制
    
    print("\n" + "=" * 60)
    print(f"测试完成：{success_count}/{len(test_cases)} 成功")
    print("=" * 60)

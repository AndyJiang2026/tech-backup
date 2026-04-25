#!/bin/bash
# 通义万相图像生成测试（curl 版本）

API_KEY="sk-a6e9b4cd251d467eaaa76d0e7a82405f"

echo "======================================"
echo "🚀 通义万相 wan2.7-image-pro 测试"
echo "======================================"

# 测试 1：动物摄影
echo ""
echo "【测试 1：可爱熊猫】"
echo "提示词：一只可爱的熊猫在吃竹子，高清摄影风格，自然光线"
echo "--------------------------------------"

RESPONSE=$(curl -s -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "wan2.7-image-pro",
    "input": {
      "prompt": "一只可爱的熊猫在吃竹子，高清摄影风格，自然光线，细节丰富"
    },
    "parameters": {
      "size": "1024x1024",
      "n": 1
    }
  }')

echo "响应："
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

# 测试 2：科技场景
echo ""
echo "【测试 2：未来科技城市】"
echo "提示词：未来科技城市，赛博朋克风格，霓虹灯光，蓝紫色调"
echo "--------------------------------------"

RESPONSE=$(curl -s -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "wan2.7-image-pro",
    "input": {
      "prompt": "未来科技城市，赛博朋克风格，霓虹灯光，蓝紫色调，3D 渲染"
    },
    "parameters": {
      "size": "1024x1024",
      "n": 1
    }
  }')

echo "响应："
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

# 测试 3：长征英雄海报
echo ""
echo "【测试 3：长征英雄电影海报】"
echo "提示词：红色教育主题电影海报，史诗庄重，中国红 + 金色，雪山剪影"
echo "--------------------------------------"

RESPONSE=$(curl -s -X POST "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "wan2.7-image-pro",
    "input": {
      "prompt": "红色教育主题电影海报，史诗庄重，历史厚重感，中国红和金色配色，雪山剪影，红军战士轮廓，五角星装饰，电影级质感，对称式构图"
    },
    "parameters": {
      "size": "1024x1024",
      "n": 1,
      "style": "<default>"
    }
  }')

echo "响应："
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

echo ""
echo "======================================"
echo "测试完成"
echo "======================================"

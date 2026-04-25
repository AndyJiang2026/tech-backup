#!/bin/bash
# MiniMax 图像生成测试

API_KEY="sk-api-SWx6QpGZbDtU2mqFQ3WWcYAHvxp2P1wfHdtnsjIAmieodllJDC1qSmKO8TcKkRbEsi7UxPd7NHOfat7oD3Td81FB-guiL3LOPIcsDUwX3RImapFqmNt1ZJo"

echo "======================================"
echo "🚀 MiniMax 图像生成测试"
echo "======================================"

# 测试 1：可爱熊猫
echo ""
echo "【测试 1：可爱熊猫】"
echo "提示词：一只可爱的熊猫在吃竹子，高清摄影风格"
echo "--------------------------------------"

RESPONSE=$(curl -s -X POST "https://api.minimax.chat/v1/file/image" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sea-1.0",
    "prompt": "一只可爱的熊猫在吃竹子，高清摄影风格，自然光线，细节丰富",
    "n": 1,
    "size": "1024x1024"
  }')

echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

# 测试 2：长征英雄海报
echo ""
echo "【测试 2：长征英雄海报】"
echo "提示词：红色教育主题电影海报，史诗庄重，中国红 + 金色"
echo "--------------------------------------"

RESPONSE=$(curl -s -X POST "https://api.minimax.chat/v1/file/image" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sea-1.0",
    "prompt": "红色教育主题电影海报，史诗庄重，历史厚重感，中国红和金色配色，雪山剪影，红军战士轮廓，五角星装饰，电影级质感",
    "n": 1,
    "size": "1024x1024"
  }')

echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

echo ""
echo "======================================"
echo "测试完成"
echo "======================================"

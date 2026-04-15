#!/bin/bash
# 钉盘 API 权限测试脚本
# 测试时间：2026-04-16

# 配置信息
CLIENT_ID="dingd1actonjhn5cexyu"
CLIENT_SECRET="KT8_62Ra7S4rzbZEFpp4xwN4X2URQrMOoFb6aQpkm35p1WLAWsFlUZTRetsbQ8rL"
AGENT_ID="4336634376"

echo "🔐 钉盘 API 权限测试"
echo "===================="
echo ""

# 步骤 1：获取 Access Token
echo "1️⃣ 获取 Access Token..."
TOKEN_RESPONSE=$(curl -s -X POST "https://api.dingtalk.com/v1.0/oauth2/accessToken" \
  -H "Content-Type: application/json" \
  -d "{
    \"appKey\": \"$CLIENT_ID\",
    \"appSecret\": \"$CLIENT_SECRET\"
  }")

echo "响应：$TOKEN_RESPONSE"
echo ""

# 提取 access_token
ACCESS_TOKEN=$(echo $TOKEN_RESPONSE | grep -o '"accessToken":"[^"]*' | cut -d'"' -f4)

if [ -z "$ACCESS_TOKEN" ]; then
  echo "❌ 获取 Access Token 失败"
  exit 1
fi

echo "✅ Access Token 获取成功"
echo "Token: ${ACCESS_TOKEN:0:20}..."
echo ""

# 步骤 2：测试钉盘空间查询
echo "2️⃣ 测试钉盘空间查询..."
CSPACE_RESPONSE=$(curl -s -X GET "https://oapi.dingtalk.com/cspace/list?access_token=$ACCESS_TOKEN" \
  -H "Content-Type: application/json")

echo "响应：$CSPACE_RESPONSE"
echo ""

# 检查是否有权限错误
if echo "$CSPACE_RESPONSE" | grep -q "InvalidAction.NotFound"; then
  echo "❌ 钉盘 API 无权限（InvalidAction.NotFound）"
  echo "提示：请在钉钉开发者后台添加钉盘文件读写权限"
  exit 1
elif echo "$CSPACE_RESPONSE" | grep -q "errcode.*0"; then
  echo "✅ 钉盘空间查询成功"
else
  echo "⚠️ 响应异常，请检查"
fi

echo ""
echo "===================="
echo "测试完成！"

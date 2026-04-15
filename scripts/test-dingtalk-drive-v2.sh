#!/bin/bash
# 钉盘 API 权限测试脚本 v2（使用新版 API）
# 测试时间：2026-04-16

# 配置信息
CLIENT_ID="dingd1actonjhn5cexyu"
CLIENT_SECRET="KT8_62Ra7S4rzbZEFpp4xwN4X2URQrMOoFb6aQpkm35p1WLAWsFlUZTRetsbQ8rL"
AGENT_ID="4336634376"

echo "🔐 钉盘 API 权限测试（新版 API）"
echo "================================"
echo ""

# 步骤 1：获取 Access Token
echo "1️⃣ 获取 Access Token..."
TOKEN_RESPONSE=$(curl -s -X POST "https://api.dingtalk.com/v1.0/oauth2/accessToken" \
  -H "Content-Type: application/json" \
  -d "{
    \"appKey\": \"$CLIENT_ID\",
    \"appSecret\": \"$CLIENT_SECRET\"
  }")

ACCESS_TOKEN=$(echo $TOKEN_RESPONSE | grep -o '"accessToken":"[^"]*' | cut -d'"' -f4)

if [ -z "$ACCESS_TOKEN" ]; then
  echo "❌ 获取 Access Token 失败"
  exit 1
fi

echo "✅ Access Token: ${ACCESS_TOKEN:0:20}..."
echo ""

# 步骤 2：测试新版钉盘 API - 获取用户空间
echo "2️⃣ 测试新版钉盘 API（v1.0/cspaces）..."
CSPACE_RESPONSE=$(curl -s -X GET "https://oapi.dingtalk.com/v1.0/cspaces" \
  -H "x-acs-dingtalk-access-token: $ACCESS_TOKEN" \
  -H "Content-Type: application/json")

echo "响应：$CSPACE_RESPONSE"
echo ""

# 检查结果
if echo "$CSPACE_RESPONSE" | grep -q '"errcode":404'; then
  echo "❌ API 404 - 端点不存在"
elif echo "$CSPACE_RESPONSE" | grep -q 'InvalidAction'; then
  echo "❌ 权限错误 - 钉盘 API 未授权"
elif echo "$CSPACE_RESPONSE" | grep -q 'cspaces'; then
  echo "✅ 钉盘 API 调用成功！"
else
  echo "⚠️ 响应异常，需进一步分析"
fi

echo ""

# 步骤 3：测试文件上传 API
echo "3️⃣ 测试文件上传 API..."
UPLOAD_RESPONSE=$(curl -s -X POST "https://oapi.dingtalk.com/v1.0/cspace/files" \
  -H "x-acs-dingtalk-access-token: $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"fileName\": \"test.txt\",
    \"fileSize\": 100,
    \"parentId\": \"root\"
  }")

echo "响应：$UPLOAD_RESPONSE"
echo ""

if echo "$UPLOAD_RESPONSE" | grep -q 'fileId\|uploadId'; then
  echo "✅ 文件上传 API 可用！"
else
  echo "⚠️ 文件上传 API 响应异常"
fi

echo ""
echo "================================"
echo "测试完成！"

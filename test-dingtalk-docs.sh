#!/bin/bash
# 钉钉文档 API 测试脚本

# 配置
CLIENT_ID="dingd1actonjhn5cexyu"
CLIENT_SECRET="KT8_62Ra7S4rzbZEFpp4xwN4X2URQrMOoFb6aQpkm35p1WLAWsFlUZTRetsbQ8rL"
SPACE_ID="VJqzq53pjZn1EzYE"

# 获取 access_token
echo "📝 正在获取 access_token..."
TOKEN_RESPONSE=$(curl -s -X POST "https://api.dingtalk.com/v1.0/oauth2/accessToken" \
  -H "Content-Type: application/json" \
  -d "{
    \"appKey\": \"$CLIENT_ID\",
    \"appSecret\": \"$CLIENT_SECRET\"
  }")

ACCESS_TOKEN=$(echo $TOKEN_RESPONSE | grep -o '"accessToken":"[^"]*"' | cut -d'"' -f4)

if [ -z "$ACCESS_TOKEN" ]; then
  echo "❌ 获取 access_token 失败"
  echo "响应：$TOKEN_RESPONSE"
  exit 1
fi

echo "✅ access_token 获取成功：${ACCESS_TOKEN:0:20}..."

# 测试 1：搜索文档
echo ""
echo "🔍 测试 1：搜索文档..."
SEARCH_RESPONSE=$(curl -s -X POST "https://api.dingtalk.com/v1.0/doc/docs/search" \
  -H "Content-Type: application/json" \
  -H "x-acs-dingtalk-access-token: $ACCESS_TOKEN" \
  -d "{
    \"keyword\": \"制度\",
    \"spaceId\": \"$SPACE_ID\",
    \"maxResults\": 5
  }")

echo "搜索结果：$SEARCH_RESPONSE" | head -c 500
echo ""

# 测试 2：列出空间文档
echo ""
echo "📋 测试 2：列出空间文档..."
LIST_RESPONSE=$(curl -s -X GET "https://api.dingtalk.com/v1.0/doc/spaces/$SPACE_ID/dentries?maxResults=10" \
  -H "x-acs-dingtalk-access-token: $ACCESS_TOKEN")

echo "文档列表：$LIST_RESPONSE" | head -c 500
echo ""

# 测试 3：尝试创建测试文档
echo ""
echo "📝 测试 3：创建测试文档..."
CREATE_RESPONSE=$(curl -s -X POST "https://api.dingtalk.com/v1.0/doc/spaces/$SPACE_ID/docs" \
  -H "Content-Type: application/json" \
  -H "x-acs-dingtalk-access-token: $ACCESS_TOKEN" \
  -d "{
    \"spaceId\": \"$SPACE_ID\",
    \"parentDentryId\": \"\",
    \"name\": \"[测试] API 访问测试 $(date +%Y-%m-%d)\",
    \"docType\": \"alidoc\"
  }")

echo "创建结果：$CREATE_RESPONSE"
echo ""

# 解析 docId
DOC_ID=$(echo $CREATE_RESPONSE | grep -o '"docId":"[^"]*"' | cut -d'"' -f4)

if [ -n "$DOC_ID" ]; then
  echo "✅ 文档创建成功！docId: $DOC_ID"
  
  # 测试 4：追加内容
  echo ""
  echo "✏️ 测试 4：追加内容到文档..."
  APPEND_RESPONSE=$(curl -s -X POST "https://api.dingtalk.com/v1.0/doc/documents/$DOC_ID/blocks/root/children" \
    -H "Content-Type: application/json" \
    -H "x-acs-dingtalk-access-token: $ACCESS_TOKEN" \
    -d "{
      \"blockType\": \"PARAGRAPH\",
      \"body\": {
        \"text\": \"这是通过 API 自动追加的测试内容。\\n\\n测试时间：$(date '+%Y-%m-%d %H:%M:%S')\\n测试目的：验证钉钉文档 API 写入权限\"
      },
      \"index\": -1
    }")
  
  echo "追加结果：$APPEND_RESPONSE"
else
  echo "⚠️ 文档创建失败，可能是权限不足"
fi

echo ""
echo "=========================================="
echo "测试完成！"
echo "=========================================="

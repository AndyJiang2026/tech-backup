#!/bin/bash
# 通义万相图像生成测试（修复 size 参数）

API_KEY="sk-a6e9b4cd251d467eaaa76d0e7a82405f"
BASE_URL="https://dashscope.aliyuncs.com/api/v1"

echo "======================================"
echo "🚀 通义万相 wanx-v1 测试（修复版）"
echo "======================================"

# 创建任务（使用正确的 size）
create_task() {
    local prompt="$1"
    local desc="$2"
    
    echo ""
    echo "【$desc】"
    echo "提示词：$prompt"
    echo "--------------------------------------"
    
    RESPONSE=$(curl -s -X POST "$BASE_URL/services/aigc/text2image/image-synthesis" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -H "X-DashScope-Async: enable" \
      -d "{
        \"model\": \"wanx-v1\",
        \"input\": {
          \"prompt\": \"$prompt\"
        },
        \"parameters\": {
          \"size\": \"1024*1024\",
          \"n\": 1
        }
      }")
    
    echo "创建任务响应：$RESPONSE"
    
    TASK_ID=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('output',{}).get('task_id',''))" 2>/dev/null)
    
    if [ -z "$TASK_ID" ]; then
        echo "❌ 任务创建失败"
        return 1
    fi
    
    echo "✅ 任务 ID: $TASK_ID"
    echo "$TASK_ID"
}

# 测试 1
TASK1=$(create_task "一只可爱的熊猫在吃竹子，高清摄影风格" "测试 1：动物摄影")
echo ""

# 测试 2
TASK2=$(create_task "红色教育主题电影海报，史诗庄重，中国红和金色配色，雪山剪影" "测试 2：长征英雄海报")
echo ""

echo "任务创建完成，等待查询..."

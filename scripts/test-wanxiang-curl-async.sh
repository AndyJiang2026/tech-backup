#!/bin/bash
# 通义万相异步图像生成测试

API_KEY="sk-a6e9b4cd251d467eaaa76d0e7a82405f"
BASE_URL="https://dashscope.aliyuncs.com/api/v1"

echo "======================================"
echo "🚀 通义万相 wanx-v1 异步测试"
echo "======================================"

# 创建任务函数
create_task() {
    local prompt="$1"
    local desc="$2"
    
    echo ""
    echo "【$desc】"
    echo "提示词：$prompt"
    echo "--------------------------------------"
    
    # 创建异步任务
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
          \"size\": \"1024x1024\",
          \"n\": 1
        }
      }")
    
    echo "创建任务响应：$RESPONSE"
    
    # 提取 task_id
    TASK_ID=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('output',{}).get('task_id',''))" 2>/dev/null)
    
    if [ -z "$TASK_ID" ]; then
        echo "❌ 任务创建失败"
        return 1
    fi
    
    echo "✅ 任务 ID: $TASK_ID"
    
    # 轮询状态
    for i in {1..30}; do
        sleep 2
        STATUS_RESPONSE=$(curl -s -X GET "$BASE_URL/tasks/$TASK_ID" \
          -H "Authorization: Bearer $API_KEY" \
          -H "Content-Type: application/json")
        
        TASK_STATUS=$(echo "$STATUS_RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('output',{}).get('task_status',''))" 2>/dev/null)
        
        echo "⏳ 第 $i 次查询 - 状态：$TASK_STATUS"
        
        if [ "$TASK_STATUS" = "SUCCEEDED" ]; then
            echo "✅ 生成成功！"
            IMG_URL=$(echo "$STATUS_RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('output',{}).get('results',[{}])[0].get('url',''))" 2>/dev/null)
            echo "🖼️ 图片 URL: $IMG_URL"
            return 0
        elif [ "$TASK_STATUS" = "FAILED" ]; then
            echo "❌ 生成失败"
            return 1
        fi
    done
    
    echo "⏰ 超时"
    return 1
}

# 测试用例
create_task "一只可爱的熊猫在吃竹子，高清摄影风格，自然光线" "测试 1：动物摄影"
sleep 3

create_task "红色教育主题电影海报，史诗庄重，历史厚重感，中国红和金色配色，雪山剪影，红军战士轮廓，五角星装饰" "测试 2：长征英雄海报"
sleep 3

create_task "未来科技城市，赛博朋克风格，霓虹灯光，蓝紫色调，3D 渲染" "测试 3：科技场景"

echo ""
echo "======================================"
echo "测试完成"
echo "======================================"

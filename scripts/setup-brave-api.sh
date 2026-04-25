#!/bin/bash
# Brave Search API Key 快速配置脚本

echo "🔍 Brave Search API Key 配置"
echo "============================"
echo ""
echo "获取 API Key 步骤："
echo "1. 访问：https://brave.com/search/api/"
echo "2. 点击 'Get Started' 注册账号"
echo "3. 创建 API Key (免费额度：每日 2000 次查询)"
echo "4. 复制 API Key"
echo ""
echo "免费额度说明："
echo "- 每日 2000 次查询"
echo "- 无需信用卡"
echo "- 即时生效"
echo ""
read -p "请输入你的 Brave API Key: " BRAVE_KEY

if [ -z "$BRAVE_KEY" ]; then
    echo "❌ 未输入 API Key，配置取消"
    exit 1
fi

# 配置到 openclaw
echo ""
echo "正在配置..."
openclaw configure --section web << EOF
$BRAVE_KEY
EOF

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Brave API Key 配置成功！"
    echo ""
    echo "测试命令："
    echo "  openclaw status --deep"
    echo ""
    echo "或者在聊天中测试："
    echo "  '帮我搜索一下 OpenClaw 最新版本特性'"
else
    echo ""
    echo "❌ 配置失败，请手动执行："
    echo "  openclaw configure --section web"
fi

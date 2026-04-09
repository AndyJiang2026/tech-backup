#!/bin/bash
# OpenClaw 升级回滚脚本
# 回滚到版本：2026.3.13
# 使用方法：bash 升级回滚脚本 -2026-04-03.sh

set -e  # 遇到错误立即退出

echo "=========================================="
echo "🔄 OpenClaw 回滚脚本"
echo "目标版本：2026.3.13"
echo "执行时间：$(date)"
echo "=========================================="

# 检查备份是否存在
if [ ! -f /home/admin/.openclaw/openclaw.json.backup.20260403.2350 ]; then
    echo "❌ 错误：备份文件不存在！"
    echo "请检查：/home/admin/.openclaw/openclaw.json.backup.20260403.2350"
    exit 1
fi

# 步骤 1: 停止 Gateway
echo ""
echo "🛑 步骤 1/4: 停止 Gateway..."
openclaw gateway stop 2>&1 || sudo systemctl stop openclaw 2>&1 || echo "Gateway 已停止"
sleep 3
echo "✅ Gateway 已停止"

# 步骤 2: 恢复配置
echo ""
echo "📁 步骤 2/4: 恢复配置文件..."
sudo cp /home/admin/.openclaw/openclaw.json.backup.20260403.2350 \
  /home/admin/.openclaw/openclaw.json
echo "✅ 配置已恢复"

# 步骤 3: 回滚版本
echo ""
echo "⬇️  步骤 3/4: 回滚 OpenClaw 版本..."
echo "当前版本："
openclaw --version
sudo npm install -g openclaw@2026.3.13
echo "回滚后版本："
openclaw --version
echo "✅ 版本回滚完成"

# 步骤 4: 重启 Gateway
echo ""
echo "🔄 步骤 4/4: 重启 Gateway..."
openclaw gateway start 2>&1 || sudo systemctl start openclaw 2>&1
sleep 5
echo "✅ Gateway 已重启"

# 验证
echo ""
echo "=========================================="
echo "✅ 回滚完成！"
echo "=========================================="
echo ""
echo "=== 验证信息 ==="
echo "版本："
openclaw --version
echo ""
echo "Gateway 状态："
openclaw gateway status 2>&1 | head -10
echo ""
echo "📋 请验证以下功能："
echo "□ 钉钉消息收发"
echo "□ QQ 机器人功能"
echo "□ 模型调用"
echo ""

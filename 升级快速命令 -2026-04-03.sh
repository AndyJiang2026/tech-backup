#!/bin/bash
# OpenClaw 升级脚本 - 2026.3.28
# 执行时间：2026-04-03 23:50
# 使用方法：bash 升级快速命令 -2026-04-03.sh

set -e  # 遇到错误立即退出

echo "=========================================="
echo "🚀 OpenClaw 升级脚本"
echo "目标版本：2026.3.28"
echo "执行时间：$(date)"
echo "=========================================="

# 步骤 1: 备份
echo ""
echo "📦 步骤 1/6: 备份配置文件..."
sudo cp /home/admin/.openclaw/openclaw.json \
  /home/admin/.openclaw/openclaw.json.backup.20260403.2350
echo "✅ 配置备份完成"

echo ""
echo "📦 备份工作空间..."
tar -czf /tmp/openclaw-backup-20260403.tar.gz \
  --exclude='extensions' \
  -C /home/admin/.openclaw .
echo "✅ 工作空间备份完成"

# 步骤 2: 验证备份
echo ""
echo "🔍 步骤 2/6: 验证备份..."
ls -lh /home/admin/.openclaw/openclaw.json.backup.20260403.2350
ls -lh /tmp/openclaw-backup-20260403.tar.gz
echo "✅ 备份验证完成"

# 步骤 3: 修复权限
echo ""
echo "🔧 步骤 3/6: 修复文件权限..."
sudo chown admin:admin /home/admin/.openclaw/openclaw.json
sudo chmod 644 /home/admin/.openclaw/openclaw.json
echo "✅ 权限修复完成"

# 步骤 4: 升级
echo ""
echo "⬆️  步骤 4/6: 升级 OpenClaw..."
echo "当前版本："
openclaw --version
sudo npm install -g openclaw@2026.3.28
echo "升级后版本："
openclaw --version
echo "✅ 升级完成"

# 步骤 5: 重启 Gateway
echo ""
echo "🔄 步骤 5/6: 重启 Gateway..."
openclaw gateway stop 2>&1 || echo "Gateway 已停止"
sleep 3
openclaw gateway start 2>&1
sleep 5
echo "✅ Gateway 重启完成"

# 步骤 6: 验证
echo ""
echo "✅ 步骤 6/6: 验证升级..."
echo "=== 版本验证 ==="
openclaw --version

echo ""
echo "=== Gateway 状态 ==="
openclaw gateway status 2>&1 | head -20

echo ""
echo "=== 插件目录 ==="
ls -la /home/admin/.openclaw/extensions/

echo ""
echo "=== 配置验证 ==="
cat /home/admin/.openclaw/openclaw.json | python3 -m json.tool > /dev/null && echo "✅ JSON 格式正确" || echo "❌ JSON 格式错误"

echo ""
echo "=========================================="
echo "🎉 升级完成！"
echo "=========================================="
echo ""
echo "📋 后续验证清单："
echo "□ 钉钉消息收发测试"
echo "□ QQ 机器人功能测试"
echo "□ 模型调用测试"
echo "□ 工作空间文件检查"
echo ""
echo "📁 备份文件位置："
echo "  - /home/admin/.openclaw/openclaw.json.backup.20260403.2350"
echo "  - /tmp/openclaw-backup-20260403.tar.gz"
echo ""
echo "🔄 如需回滚，执行："
echo "  sudo npm install -g openclaw@2026.3.13"
echo "  sudo cp /home/admin/.openclaw/openclaw.json.backup.20260403.2350 /home/admin/.openclaw/openclaw.json"
echo "  openclaw gateway restart"
echo ""

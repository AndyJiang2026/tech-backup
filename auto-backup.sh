#!/bin/bash

# 🐴 强国小马自动备份脚本
# 用途：自动提交配置变更并推送到 GitHub + OSS

set -e

# 进入工作区目录
cd /home/admin/.openclaw/workspace-chief-agent || exit 1

echo "========================================"
echo "🐴 强国小马自动备份"
echo "========================================"
echo "备份时间：$(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 配置 Git 用户信息
git config user.name "强国小马"
git config user.email "chief-agent@openclaw.local"

# 1. Git 备份
echo "📦 1. Git 备份..."
echo ""

# 添加所有改动
git add .

# 检查是否有改动需要提交
if git diff --staged --quiet; then
    echo "   ✅ 无新改动，跳过 Git 提交"
else
    # 提交改动
    git commit -m "🐴 自动备份：$(date '+%Y-%m-%d %H:%M:%S')"
    echo "   ✅ Git 提交完成"
fi

# 推送到 GitHub
git push origin master
if [ $? -eq 0 ]; then
    echo "   ✅ 推送成功到 GitHub"
else
    echo "   ❌ 推送失败，请检查网络连接"
    exit 1
fi

echo ""

# 2. OSS 备份（可选）
echo "📦 2. OSS 备份..."
if [ -f ~/.ossutilconfig ] && command -v ossutil64 &> /dev/null; then
    echo "   ✅ OSS 配置已就绪，执行备份..."
    /home/admin/.openclaw/scripts/oss-backup.sh
else
    echo "   ⚠️  OSS 未配置，跳过 OSS 备份"
    echo "   提示：运行以下命令配置 OSS："
    echo "   wget https://gosspublic.alicdn.com/ossutil/install.sh && bash install.sh"
    echo "   ossutil64 config"
fi

echo ""
echo "========================================"
echo "✅ 备份完成！"
echo "========================================"
echo ""
echo "备份位置:"
echo "  - GitHub: git@github.com:AndyJiang2026/tech-backup.git"
echo "  - OSS: oss://qiangguo-xiaoma-backup/openclaw/"
echo ""

#!/bin/bash

# 🐴 强国小马自动备份脚本
# 用途：自动提交配置变更并推送到 GitHub

# 进入工作区目录
cd /home/admin/.openclaw/workspace-chief-agent || exit 1

echo "🐴 强国小马配置备份开始 - $(date '+%Y-%m-%d %H:%M:%S')"

# 配置 Git 用户信息
git config user.name "强国小马"
git config user.email "chief-agent@openclaw.local"

# 添加所有改动
git add .

# 检查是否有改动需要提交
if git diff --staged --quiet; then
    echo "✅ 无新改动，跳过提交"
else
    # 提交改动
    git commit -m "🐴 自动备份：$(date '+%Y-%m-%d %H:%M:%S')"
    echo "✅ 提交完成"
fi

# 推送到 GitHub
git push origin master
if [ $? -eq 0 ]; then
    echo "✅ 推送成功到 GitHub"
else
    echo "❌ 推送失败，请检查网络连接"
    exit 1
fi

echo "🐴 备份完成 - $(date '+%Y-%m-%d %H:%M:%S')"

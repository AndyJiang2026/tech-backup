#!/bin/bash

# 🐴 强国小马 - OpenClaw 全面健康检查脚本
# 用途：系统性地检测 OpenClaw 的各项健康指标

echo "========================================"
echo "🐴 OpenClaw 全面健康检查"
echo "========================================"
echo "检查时间：$(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 检查计数器
TOTAL=0
PASS=0
WARN=0
FAIL=0

# 检查函数
check_item() {
    local name="$1"
    local command="$2"
    TOTAL=$((TOTAL + 1))
    
    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✅${NC} $name"
        PASS=$((PASS + 1))
        return 0
    else
        echo -e "${RED}❌${NC} $name"
        FAIL=$((FAIL + 1))
        return 1
    fi
}

warn_item() {
    local name="$1"
    local condition="$2"
    TOTAL=$((TOTAL + 1))
    
    if eval "$condition"; then
        echo -e "${YELLOW}⚠️${NC} $name"
        WARN=$((WARN + 1))
        return 1
    else
        echo -e "${GREEN}✅${NC} $name"
        PASS=$((PASS + 1))
        return 0
    fi
}

echo "1️⃣  系统资源检查"
echo "----------------------------------------"
check_item "  OpenClaw 进程运行" "ps aux | grep openclaw | grep -v grep"
check_item "  Gateway 端口监听 (16023)" "netstat -tlnp 2>/dev/null | grep 16023 || ss -tlnp | grep 16023"
check_item "  Node.js 已安装" "node -v"
warn_item "  CPU 使用率 <90%" "[ \$(top -bn1 | grep 'Cpu(s)' | awk '{print \$2}' | cut -d'%' -f1 | cut -d'.' -f1) -lt 90 ]"
warn_item "  内存使用率 <80%" "[ \$(free | grep Mem | awk '{print \$3/\$2 * 100.0}' | cut -d'.' -f1) -lt 80 ]"
warn_item "  磁盘使用率 <80%" "[ \$(df / | tail -1 | awk '{print \$5}' | cut -d'%' -f1) -lt 80 ]"
echo ""

echo "2️⃣  OpenClaw 核心组件"
echo "----------------------------------------"
check_item "  openclaw CLI 可用" "openclaw --version"
check_item "  Gateway 服务运行" "ps aux | grep openclaw-gateway | grep -v grep"
check_item "  Browser 控制可用" "ps aux | grep chrome | grep remote-debugging"
check_item "  DingTalk 连接器" "ls /home/admin/.openclaw/extensions/dingtalk-connector"
echo ""

echo "3️⃣  Agent 配置检查"
echo "----------------------------------------"
check_item "  chief-agent 配置" "cat /home/admin/.openclaw/agents/business-team/agent.json"
check_item "  ops-agent 配置" "cat /home/admin/.openclaw/agents/business-team/ops-agent.json"
check_item "  finance-agent 配置" "cat /home/admin/.openclaw/agents/business-team/finance-agent.json"
check_item "  legal-agent 配置" "cat /home/admin/.openclaw/agents/business-team/legal-agent.json"
check_item "  copywriter-agent 配置" "cat /home/admin/.openclaw/agents/business-team/copywriter-agent.json"
check_item "  design-agent 配置" "cat /home/admin/.openclaw/agents/business-team/design-agent.json"
echo ""

echo "4️⃣  安全策略检查"
echo "----------------------------------------"
check_item "  Red Lines 策略文件" "cat /home/admin/.openclaw/workspace/config/red-lines-policy.json"
check_item "  SSH 密钥存在" "ls ~/.ssh/id_ed25519"
check_item "  Git 远程配置" "cd /home/admin/.openclaw/workspace-chief-agent && git remote -v"
echo ""

echo "5️⃣  API 配置检查"
echo "----------------------------------------"
check_item "  MiniMax API Key" "grep MINIMAX_API_KEY ~/.bashrc"
check_item "  SearXNG 配置" "grep SEARXNG_URL ~/.bashrc"
check_item "  DashScope 配置" "cat /home/admin/.openclaw/agents/chief-agent/agent/models.json"
echo ""

echo "6️⃣  备份状态检查"
echo "----------------------------------------"
check_item "  Git 仓库存在" "ls /home/admin/.openclaw/workspace-chief-agent/.git"
check_item "  备份目录存在" "ls /home/admin/.openclaw/backup"
check_item "  自动备份脚本" "ls /home/admin/.openclaw/workspace-chief-agent/auto-backup.sh"
check_item "  Cron 任务配置" "crontab -l 2>/dev/null | grep -E 'backup|audit'"
echo ""

echo "7️⃣  技能安装检查"
echo "----------------------------------------"
check_item "  skills 目录存在" "ls /home/admin/.openclaw/workspace/skills"
check_item "  healthcheck 技能" "ls /usr/local/lib/node_modules/openclaw/skills/healthcheck"
check_item "  searxng 技能" "ls /home/admin/.openclaw/workspace/skills/searxng"
echo ""

echo "8️⃣  日志和监控"
echo "----------------------------------------"
check_item "  日志目录存在" "ls /home/admin/.openclaw/logs"
check_item "  配置监控日志" "ls /home/admin/.openclaw/logs/cron-config-watch.log"
check_item "  内存文件" "ls /home/admin/.openclaw/workspace-chief-agent/memory"
echo ""

echo "========================================"
echo "📊 健康检查总结"
echo "========================================"
echo "总检查项：$TOTAL"
echo -e "${GREEN}通过：$PASS${NC}"
echo -e "${YELLOW}警告：$WARN${NC}"
echo -e "${RED}失败：$FAIL${NC}"
echo ""

# 计算健康度
if [ $TOTAL -gt 0 ]; then
    HEALTH_SCORE=$((PASS * 100 / TOTAL))
    echo "健康度评分：$HEALTH_SCORE/100"
    
    if [ $HEALTH_SCORE -ge 90 ]; then
        echo -e "${GREEN}状态：优秀 🟢${NC}"
    elif [ $HEALTH_SCORE -ge 70 ]; then
        echo -e "${YELLOW}状态：良好 🟡${NC}"
    else
        echo -e "${RED}状态：需要关注 🔴${NC}"
    fi
fi
echo ""

# 生成报告
REPORT_FILE="/home/admin/.openclaw/workspace-chief-agent/reports/health-check-$(date +%Y-%m-%d-%H-%M-%S).md"
cat > "$REPORT_FILE" << EOF
# 🐴 OpenClaw 健康检查报告

**检查时间**: $(date '+%Y-%m-%d %H:%M:%S')

## 📊 检查结果

| 指标 | 数量 |
|------|------|
| 总检查项 | $TOTAL |
| 通过 | $PASS |
| 警告 | $WARN |
| 失败 | $FAIL |

## 健康度评分

**$HEALTH_SCORE/100**

EOF

echo "📝 报告已生成：$REPORT_FILE"
echo ""
echo "========================================"

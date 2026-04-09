#!/bin/bash

# 🐴 强国小马 - SearXNG 配置优化脚本
# 用途：自动优化 SearXNG 搜索引擎配置，提升中国大陆搜索效果

set -e

echo "========================================"
echo "🐴 SearXNG 配置优化脚本"
echo "========================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# 检查 Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker 未安装${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Docker 已安装${NC}"

# 检查 SearXNG 容器
if ! sudo docker ps | grep -q searxng; then
    echo -e "${RED}❌ SearXNG 容器未运行${NC}"
    exit 1
fi
echo -e "${GREEN}✅ SearXNG 容器运行中${NC}"

# 创建优化配置文件
echo ""
echo "📝 创建优化配置文件..."

CONFIG_DIR="/opt/searxng/config"
sudo mkdir -p $CONFIG_DIR

# 创建 settings.yml（中国大陆优化版）
sudo bash -c 'cat > '"$CONFIG_DIR"'/settings.yml << EOF
# SearXNG 配置 - 中国大陆优化版
# 创建时间：$(date)

use_default_settings: true

general:
  debug: false
  instance_name: "强国小马搜索"
  donation_url: false
  contact_url: false
  enable_metrics: false

search:
  safe_search: 0
  autocomplete: "baidu"
  default_lang: "zh-CN"
  default_category: "general"
  formats:
    - html
    - json

server:
  secret_key: "searxng-secret-$(date +%Y%m%d)"
  limiter: false
  image_proxy: true
  http_protocol_version: "1.1"
  method: "POST"
  default_http_headers:
    X-Forwarded-For: ""
  bind_address: "0.0.0.0:8080"

ui:
  static_use_hash: true
  default_theme: simple
  theme_args:
    simple_style: auto
  infinite_scroll: false
  results_on_new_tab: false
  query_in_title: false
  center_alignment: true
  searchbar_order: "1"
  enabled_plugins:
    - "Self Information"
    - "Time zone"
    - "Unit converter"
    - "Tracker URL remover"

outgoing:
  request_timeout: 5.0
  max_request_timeout: 10.0
  pool_connections: 100
  pool_maxsize: 50
  retries: 2
  ipv6: false

# 搜索引擎配置
engines:
  # ✅ 启用 - 国内搜索引擎
  - name: 百度
    engine: baidu
    shortcut: bd
    disabled: false
    timeout: 5.0
  
  - name: 必应中国
    engine: bing
    shortcut: bing
    base_url: https://cn.bing.com/
    disabled: false
    timeout: 5.0
  
  - name: 搜狗微信
    engine: google
    shortcut: sogou
    base_url: https://weixin.sogou.com/
    disabled: false
    timeout: 5.0
  
  - name: 必应图片
    engine: bing_images
    shortcut: bi
    disabled: false
    timeout: 5.0
  
  - name: 必应视频
    engine: bing_videos
    shortcut: bv
    disabled: false
    timeout: 5.0
  
  - name: 必应新闻
    engine: bing_news
    shortcut: bn
    disabled: false
    timeout: 5.0
  
  - name: 维基百科（中文）
    engine: wikipedia
    shortcut: wp
    base_url: https://zh.wikipedia.org/
    disabled: false
    timeout: 5.0
  
  - name: 豆瓣
    engine: google
    shortcut: db
    base_url: https://www.douban.com/
    disabled: false
    timeout: 5.0
  
  # ⚠️ 禁用 - 国内访问慢的引擎
  - name: 谷歌
    engine: google
    shortcut: gg
    disabled: true
  
  - name: DuckDuckGo
    engine: duckduckgo
    shortcut: ddg
    disabled: true
  
  - name: Brave
    engine: brave
    shortcut: br
    disabled: true
  
  - name: Startpage
    engine: startpage
    shortcut: sp
    disabled: true
  
  - name: Qwant
    engine: qwant
    shortcut: qw
    disabled: true
  
  - name: Yahoo
    engine: yahoo
    shortcut: yh
    disabled: true
  
  - name: Yandex
    engine: yandex
    shortcut: yd
    disabled: true

# 插件配置
plugins:
  - name: Self Information
    enabled: true
  - name: Time zone
    enabled: true
  - name: Unit converter
    enabled: true
  - name: Tracker URL remover
    enabled: true
  - name: Hash plugin
    enabled: true

# 日志配置
logging:
  level: INFO
  format: "%(asctime)s %(levelname)s: %(message)s"
EOF'

echo -e "${GREEN}✅ 配置文件已创建${NC}"

# 重启容器
echo ""
echo "🔄 重启 SearXNG 容器以应用配置..."
sudo docker restart searxng

# 等待启动
echo "⏳ 等待服务启动..."
sleep 10

# 验证配置
echo ""
echo "🧪 验证配置..."

# 检查容器状态
if sudo docker ps | grep -q searxng; then
    echo -e "${GREEN}✅ 容器运行正常${NC}"
else
    echo -e "${RED}❌ 容器启动失败${NC}"
    exit 1
fi

# 测试网页访问
if curl -s --max-time 10 "http://localhost:8083/" | grep -q "SearXNG"; then
    echo -e "${GREEN}✅ 网页访问正常${NC}"
else
    echo -e "${YELLOW}⚠️  网页访问异常（可能还在启动中）${NC}"
fi

# 测试搜索
echo ""
echo "🔍 测试搜索功能..."
python3 /home/admin/.openclaw/scripts/searxng-search.py "OpenClaw" | head -20

echo ""
echo "========================================"
echo -e "${GREEN}✅ 配置优化完成！${NC}"
echo "========================================"
echo ""
echo "📍 访问地址:"
echo "   本地：http://localhost:8083"
echo "   公网：http://39.106.35.229:8083"
echo ""
echo "🎯 已启用的搜索引擎:"
echo "   ✅ 百度"
echo "   ✅ 必应中国"
echo "   ✅ 搜狗微信"
echo "   ✅ 必应图片/视频/新闻"
echo "   ✅ 维基百科（中文）"
echo "   ✅ 豆瓣"
echo ""
echo "🚫 已禁用的搜索引擎:"
echo "   ❌ 谷歌（国内访问慢）"
echo "   ❌ DuckDuckGo（国内访问慢）"
echo "   ❌ Brave（国内访问慢）"
echo "   ❌ 其他国外引擎"
echo ""
echo "🔧 下一步:"
echo "   1. 打开浏览器访问 http://39.106.35.229:8083"
echo "   2. 测试搜索"OpenClaw" 或 "全国大学出版社""
echo "   3. 验证搜索结果质量"
echo ""

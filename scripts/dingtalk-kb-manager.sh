#!/bin/bash
# 钉钉知识库管理工具
# 用法：./dingtalk-kb-manager.sh <command> [options]

set -e

# 配置
SPACE_ID="VJqzq53pjZn1EzYE"
CLIENT_ID="dingd1actonjhn5cexyu"
CLIENT_SECRET="KT8_62Ra7S4rzbZEFpp4xwN4X2URQrMOoFb6aQpkm35p1WLAWsFlUZTRetsbQ8rL"

# 颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 帮助信息
show_help() {
    echo -e "${BLUE}📚 钉钉知识库管理工具${NC}"
    echo ""
    echo "用法：$0 <command> [options]"
    echo ""
    echo "命令:"
    echo "  ${GREEN}list${NC}              列出知识库文档"
    echo "  ${GREEN}search${NC} <query>    搜索知识库"
    echo "  ${GREEN}upload${NC} <file>    上传文档"
    echo "  ${GREEN}delete${NC} <id>      删除文档"
    echo "  ${GREEN}stats${NC}            显示统计信息"
    echo "  ${GREEN}sync${NC}             执行同步"
    echo "  ${GREEN}help${NC}             显示帮助"
    echo ""
    echo "示例:"
    echo "  $0 list"
    echo "  $0 search \"VR 项目\""
    echo "  $0 upload document.pdf"
    echo "  $0 stats"
}

# 检查 API 权限
check_permissions() {
    echo -e "${YELLOW}⚠️  检查 API 权限...${NC}"
    echo ""
    echo "请在钉钉开放平台确认以下权限已申请:"
    echo "  - knowledge:read"
    echo "  - knowledge:write"
    echo "  - knowledge:search"
    echo "  - drive:file:read"
    echo "  - drive:file:write"
    echo ""
    echo "申请地址：https://developers.dingtalk.com/"
    echo ""
}

# 列出文档
list_documents() {
    echo -e "${BLUE}📋 知识库文档列表${NC}"
    echo "空间 ID: $SPACE_ID"
    echo ""
    
    # TODO: 调用钉钉 API
    check_permissions
    
    echo -e "${YELLOW}⚠️  需要 API 权限才能获取文档列表${NC}"
}

# 搜索文档
search_documents() {
    QUERY=$1
    
    if [ -z "$QUERY" ]; then
        echo -e "${RED}错误：请提供搜索关键词${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}🔍 搜索知识库${NC}"
    echo "关键词：$QUERY"
    echo ""
    
    # TODO: 调用钉钉 API
    check_permissions
    
    echo -e "${YELLOW}⚠️  需要 API 权限才能搜索${NC}"
}

# 上传文档
upload_document() {
    FILE=$1
    
    if [ -z "$FILE" ]; then
        echo -e "${RED}错误：请提供文件路径${NC}"
        exit 1
    fi
    
    if [ ! -f "$FILE" ]; then
        echo -e "${RED}错误：文件不存在：$FILE${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}⬆️  上传文档${NC}"
    echo "文件：$FILE"
    echo "大小：$(du -h "$FILE" | cut -f1)"
    echo ""
    
    # TODO: 调用钉钉 API
    check_permissions
    
    echo -e "${YELLOW}⚠️  需要 API 权限才能上传${NC}"
}

# 删除文档
delete_document() {
    DOC_ID=$1
    
    if [ -z "$DOC_ID" ]; then
        echo -e "${RED}错误：请提供文档 ID${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}🗑️  删除文档${NC}"
    echo "文档 ID: $DOC_ID"
    echo ""
    
    read -p "确认删除？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "取消删除"
        exit 0
    fi
    
    # TODO: 调用钉钉 API
    check_permissions
    
    echo -e "${YELLOW}⚠️  需要 API 权限才能删除${NC}"
}

# 显示统计
show_stats() {
    echo -e "${BLUE}📊 知识库统计${NC}"
    echo ""
    
    # 本地统计
    WORKSPACE="/home/admin/.openclaw/workspace-chief-agent"
    
    echo "本地文档统计:"
    
    if [ -d "$WORKSPACE/docs" ]; then
        DOCS_COUNT=$(find "$WORKSPACE/docs" -name "*.md" -o -name "*.pdf" | wc -l)
        echo "  docs/目录：$DOCS_COUNT 个文件"
    fi
    
    if [ -d "$WORKSPACE/reports" ]; then
        REPORTS_COUNT=$(find "$WORKSPACE/reports" -name "*.md" | wc -l)
        echo "  reports/目录：$REPORTS_COUNT 个文件"
    fi
    
    if [ -d "$WORKSPACE/documents" ]; then
        DOCX_COUNT=$(find "$WORKSPACE/documents" -name "*.md" -o -name "*.docx" -o -name "*.pdf" | wc -l)
        echo "  documents/目录：$DOCX_COUNT 个文件"
    fi
    
    echo ""
    echo "钉钉知识库:"
    echo "  空间 ID: $SPACE_ID"
    echo "  状态：待 API 权限配置"
    echo ""
    
    check_permissions
}

# 执行同步
do_sync() {
    echo -e "${BLUE}🔄 执行同步${NC}"
    echo ""
    
    # 调用同步脚本
    SCRIPT_DIR="$(dirname "$0")"
    if [ -f "$SCRIPT_DIR/dingtalk-kb-sync.sh" ]; then
        bash "$SCRIPT_DIR/dingtalk-kb-sync.sh"
    else
        echo -e "${RED}错误：同步脚本不存在${NC}"
        exit 1
    fi
}

# 主逻辑
case "${1:-help}" in
    list)
        list_documents
        ;;
    search)
        search_documents "$2"
        ;;
    upload)
        upload_document "$2"
        ;;
    delete)
        delete_document "$2"
        ;;
    stats)
        show_stats
        ;;
    sync)
        do_sync
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo -e "${RED}未知命令：$1${NC}"
        echo ""
        show_help
        exit 1
        ;;
esac

#!/usr/bin/env python3
"""
🐴 强国小马 - SearXNG 搜索工具
用途：为 OpenClaw 提供搜索功能
"""

import sys
import requests
from urllib.parse import quote

SEARXNG_URL = "http://localhost:8083"

def search(query, count=10):
    """
    搜索函数
    
    Args:
        query: 搜索关键词
        count: 返回结果数量
    
    Returns:
        dict: 搜索结果
    """
    try:
        # 构建搜索 URL
        encoded_query = quote(query)
        url = f"{SEARXNG_URL}/search?q={encoded_query}&pageno=1&format=html"
        
        # 获取搜索结果页面
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml"
        }
        
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        
        # 解析 HTML 结果（简单解析）
        results = []
        html = response.text
        
        # 提取搜索结果（简化版）
        import re
        result_pattern = r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>'
        matches = re.findall(result_pattern, html)
        
        for href, title in matches[:count]:
            if href.startswith('http') and 'searxng' not in href:
                results.append({
                    "title": title.strip(),
                    "url": href,
                    "content": ""
                })
        
        output = {
            "query": query,
            "source": "SearXNG",
            "searxng_url": f"{SEARXNG_URL}/search?q={encoded_query}",
            "number_of_results": len(results),
            "results": results
        }
        
        import json
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return True
        
    except Exception as e:
        import json
        error_result = {
            "query": query,
            "error": str(e),
            "source": "SearXNG",
            "searxng_url": f"{SEARXNG_URL}/"
        }
        print(json.dumps(error_result, ensure_ascii=False, indent=2))
        return False

def main():
    """主函数"""
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"🔍 搜索：{query}")
        print(f"📍 来源：SearXNG ({SEARXNG_URL})")
        print("=" * 60)
        search(query)
    else:
        print("🐴 强国小马 - SearXNG 搜索工具")
        print("=" * 60)
        print("用法：python3 searxng-search.py <搜索关键词>")
        print("示例：python3 searxng-search.py OpenClaw Agent")
        print("=" * 60)
        print(f"🌐 网页访问：{SEARXNG_URL}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
法务专家工具 - 合同审查、法律咨询
通用版本，不依赖任何平台插件
"""

import json
import sys
from datetime import datetime

# 高风险条款关键词
HIGH_RISK_KEYWORDS = [
    "唯一合作", "排他", "最终解释权", "自动续约",
    "不得", "无权", "必须", "一律", "概不"
]

# 违约金过高标准（日息）
HIGH_PENALTY_RATE = 0.0005  # 万分之五

def analyze_contract(clause_type, text):
    """分析合同条款风险"""
    risks = []
    
    # 检查高风险关键词
    for keyword in HIGH_RISK_KEYWORDS:
        if keyword in text:
            risks.append({
                "level": "high",
                "keyword": keyword,
                "suggestion": f"包含'{keyword}'等绝对化表述，建议修改为更平等的表述"
            })
    
    # 检查违约金比例
    if "违约金" in text or "赔偿" in text:
        if "万分之" in text:
            try:
                # 提取比例
                import re
                match = re.search(r'万分之 ([ 一二三四五六七八九十\d]+)', text)
                if match:
                    rate_str = match.group(1)
                    # 简单转换
                    rate_map = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, 
                               '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}
                    if rate_str in rate_map:
                        rate = rate_map[rate_str] / 10000
                    else:
                        rate = int(rate_str) / 10000
                    
                    if rate > HIGH_PENALTY_RATE:
                        risks.append({
                            "level": "high",
                            "keyword": "违约金过高",
                            "suggestion": f"违约金日息{rate*10000:.0f}万分之过高，建议降至万分之三至万分之五"
                        })
            except:
                pass
    
    # 检查管辖法院
    if "所在地人民法院" in text:
        if "乙方所在地" in text or "甲方所在地" in text:
            risks.append({
                "level": "medium",
                "keyword": "管辖法院",
                "suggestion": "建议约定为'原告所在地'或'合同签订地'人民法院，或选择仲裁"
            })
    
    return risks

def review_contract(clauses):
    """审查整份合同"""
    report = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total_clauses": len(clauses),
        "high_risks": [],
        "medium_risks": [],
        "low_risks": [],
        "suggestions": []
    }
    
    for clause in clauses:
        clause_type = clause.get("type", "未知条款")
        text = clause.get("text", "")
        
        risks = analyze_contract(clause_type, text)
        for risk in risks:
            risk["clause_type"] = clause_type
            risk["original_text"] = text[:100] + "..." if len(text) > 100 else text
            
            if risk["level"] == "high":
                report["high_risks"].append(risk)
            elif risk["level"] == "medium":
                report["medium_risks"].append(risk)
            else:
                report["low_risks"].append(risk)
    
    # 生成建议
    if len(report["high_risks"]) > 0:
        report["suggestions"].append(f"发现{len(report['high_risks'])}处高风险条款，建议优先修改")
    if len(report["medium_risks"]) > 0:
        report["suggestions"].append(f"发现{len(report['medium_risks'])}处中风险条款，建议争取修改")
    
    return report

def generate_report(report):
    """生成审查报告"""
    output = []
    output.append("# 合同审查报告")
    output.append(f"\n**审查日期**: {report['date']}\n")
    
    # 风险汇总
    output.append("## 风险汇总\n")
    output.append(f"- 🔴 高风险条款：{len(report['high_risks'])} 处")
    output.append(f"- 🟡 中风险条款：{len(report['medium_risks'])} 处")
    output.append(f"- 🟢 低风险条款：{len(report['low_risks'])} 处\n")
    
    # 高风险条款
    if report['high_risks']:
        output.append("\n## 🔴 高风险条款\n")
        for i, risk in enumerate(report['high_risks'], 1):
            output.append(f"### {i}. {risk['clause_type']}")
            output.append(f"**关键词**: {risk['keyword']}")
            output.append(f"**原文**: {risk['original_text']}")
            output.append(f"**建议**: {risk['suggestion']}\n")
    
    # 中风险条款
    if report['medium_risks']:
        output.append("\n## 🟡 中风险条款\n")
        for i, risk in enumerate(report['medium_risks'], 1):
            output.append(f"### {i}. {risk['clause_type']}")
            output.append(f"**关键词**: {risk['keyword']}")
            output.append(f"**原文**: {risk['original_text']}")
            output.append(f"**建议**: {risk['suggestion']}\n")
    
    # 建议
    if report['suggestions']:
        output.append("\n## 💡 谈判建议\n")
        for suggestion in report['suggestions']:
            output.append(f"- {suggestion}")
    
    return "\n".join(output)

if __name__ == "__main__":
    # 示例合同条款
    sample_clauses = [
        {
            "type": "排他性条款",
            "text": "乙方为甲方上述资金申请的唯一合作人，甲方须严格为乙方的服务内容及双方合作事宜保密。"
        },
        {
            "type": "违约责任",
            "text": "如甲方逾期付款，乙方将向甲方另行加收利息，利息按应付款额每日万分之八计算，直至付清。"
        },
        {
            "type": "争议解决",
            "text": "双方因履行本协议发生的争议，应首先通过友好协商解决，协商不成时，任何一方可向乙方所在地人民法院提起诉讼解决。"
        },
        {
            "type": "付款条款",
            "text": "成功申请到政府资助金后，甲方承诺，在收到资助项目拨款后的五个工作日内，按政府拨款数额的 10%，支付乙方咨询顾问费。"
        }
    ]
    
    # 审查合同
    report = review_contract(sample_clauses)
    
    # 生成报告
    markdown_report = generate_report(report)
    print(markdown_report)
    
    # 保存报告
    with open("/home/admin/.openclaw/workspace-chief-agent/合同审查报告示例.md", "w", encoding="utf-8") as f:
        f.write(markdown_report)
    
    print("\n✅ 报告已保存到：/home/admin/.openclaw/workspace-chief-agent/合同审查报告示例.md")

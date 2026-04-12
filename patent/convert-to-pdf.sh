#!/bin/bash
# Markdown to PDF converter using Chrome

INPUT_MD="发明专利申请书 - 基于空间扭曲技术的 VR 大空间动态优化方法及系统.md"
OUTPUT_HTML="temp.html"
OUTPUT_PDF="发明专利申请书 - 基于空间扭曲技术的 VR 大空间动态优化方法及系统.pdf"

# Convert Markdown to HTML
cat > "$OUTPUT_HTML" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>发明专利申请书 - 基于空间扭曲技术的 VR 大空间动态优化方法及系统</title>
    <style>
        @page {
            size: A4;
            margin: 2.5cm;
        }
        body {
            font-family: "Noto Serif CJK SC", "SimSun", "Songti SC", serif;
            font-size: 12pt;
            line-height: 1.5;
            color: #000;
            max-width: 210mm;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            font-size: 16pt;
            text-align: center;
            margin: 30px 0 20px 0;
            font-weight: bold;
        }
        h2 {
            font-size: 14pt;
            margin: 25px 0 15px 0;
            font-weight: bold;
            border-bottom: 2px solid #000;
            padding-bottom: 5px;
        }
        h3 {
            font-size: 12pt;
            margin: 20px 0 10px 0;
            font-weight: bold;
        }
        h4 {
            font-size: 11pt;
            margin: 15px 0 8px 0;
            font-weight: bold;
        }
        p {
            margin: 10px 0;
            text-align: justify;
        }
        pre {
            font-family: "Courier New", monospace;
            font-size: 10pt;
            background: #f5f5f5;
            padding: 10px;
            border: 1px solid #ddd;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        code {
            font-family: "Courier New", monospace;
            font-size: 10pt;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        th, td {
            border: 1px solid #000;
            padding: 8px 12px;
            text-align: left;
        }
        th {
            background: #f0f0f0;
            font-weight: bold;
        }
        .abstract {
            margin: 20px 0;
            padding: 15px;
            border: 1px solid #000;
        }
        .claims {
            margin: 20px 0;
        }
        .claim-item {
            margin: 10px 0;
            text-indent: 2em;
        }
        .figure {
            margin: 30px 0;
            page-break-inside: avoid;
        }
        .figure-caption {
            text-align: center;
            font-size: 10pt;
            margin-top: 10px;
            font-style: italic;
        }
        .page-break {
            page-break-before: always;
        }
    </style>
</head>
<body>
HTMLEOF

# Simple markdown to HTML conversion (basic)
sed 's/^# \(.*\)$/<h1>\1<\/h1>/' "$INPUT_MD" | \
sed 's/^## \(.*\)$/<h2>\1<\/h2>/' | \
sed 's/^### \(.*\)$/<h3>\1<\/h3>/' | \
sed 's/^#### \(.*\)$/<h4>\1<\/h4>/' | \
sed 's/^\*\*\(.*\)\*\*$/<strong>\1<\/strong>/' | \
sed 's/^\* \(.*\)$/<li>\1<\/li>/' | \
grep -v "^---$" >> "$OUTPUT_HTML"

cat >> "$OUTPUT_HTML" << 'HTMLEOF'
</body>
</html>
HTMLEOF

# Convert HTML to PDF using Chrome
google-chrome --headless --disable-gpu --print-to-pdf="$OUTPUT_PDF" --paper-size-a4 --margin-top=25mm --margin-bottom=25mm --margin-left=25mm --margin-right=25mm "$OUTPUT_HTML"

# Cleanup
rm -f "$OUTPUT_HTML"

echo "PDF generated: $OUTPUT_PDF"

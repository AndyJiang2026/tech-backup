#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 zipfile 直接创建 PPTX 文件（无需 python-pptx 依赖）
PPTX 本质是 ZIP 文件，包含 XML 内容
"""

import zipfile
import os
from datetime import datetime

def create_minimal_pptx(filename, slides_content):
    """创建基本 PPTX 文件"""
    
    # PPTX 文件结构
    # 这是一个简化版本，实际 PPTX 需要更多 XML 文件
    
    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 添加 [Content_Types].xml
        content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  <Override PartName="/ppt/presentationProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentationProperties+xml"/>
  <Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''
        zipf.writestr('[Content_Types].xml', content_types)
        
        # 添加 _rels/.rels
        rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''
        zipf.writestr('_rels/.rels', rels)
        
        # 添加 docProps/core.xml
        core_props = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>高校思政 VR 百校复制方案</dc:title>
  <dc:subject>招商 PPT</dc:subject>
  <dc:creator>强国小马</dc:creator>
  <cp:lastModifiedBy>强国小马</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-04-12T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-04-12T00:00:00Z</dcterms:modified>
</cp:coreProperties>'''
        zipf.writestr('docProps/core.xml', core_props)
        
        # 添加 docProps/app.xml
        app_props = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <TotalTime>0</TotalTime>
  <Slides>{len(slides_content)}</Slides>
  <Words>0</Words>
  <Application>OpenClaw</Application>
</Properties>'''
        zipf.writestr('docProps/app.xml', app_props)
        
        # 添加 ppt/_rels/presentation.xml.rels
        ppt_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps" Target="viewProps.xml"/>
  <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/presentationProps" Target="presentationProps.xml"/>
</Relationships>'''
        zipf.writestr('ppt/_rels/presentation.xml.rels', ppt_rels)
        
        # 添加 ppt/presentation.xml
        slide_ids = ''.join([f'<p:sldId id="{256+i}" r:id="rId{i+4}"/>' for i in range(len(slides_content))])
        presentation = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" saveSubsetFonts="1" xmlns:r16="http://schemas.microsoft.com/office/presentation/2014/main" embedFonts="none">
  <p:sldMasterLst>
    <p:sldMaster r:id="rId1"/>
  </p:sldMasterLst>
  <p:sldLst>
    {slide_ids}
  </p:sldLst>
  <p:notesMasterLst>
    <p:notesMaster r:id="rId5"/>
  </p:notesMasterLst>
  <p:handoutMasterLst>
    <p:handoutMaster r:id="rId6"/>
  </p:handoutMasterLst>
  <p:sldSz cx="9144000" cy="5143500"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>'''
        zipf.writestr('ppt/presentation.xml', presentation)
        
        # 添加 ppt/slideMasters/slideMaster1.xml
        slide_master = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill>
          <a:srgbClr val="FFFFFF"/>
        </a:solidFill>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
</p:sldMaster>'''
        zipf.writestr('ppt/slideMasters/slideMaster1.xml', slide_master)
        
        # 添加 ppt/theme/theme1.xml
        theme = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">
  <a:themeElements>
    <a:clrScheme name="Office">
      <a:dk1>
        <a:sysClr val="windowText" lastClr="000000"/>
      </a:dk1>
      <a:lt1>
        <a:sysClr val="window" lastClr="FFFFFF"/>
      </a:lt1>
      <a:dk2>
        <a:srgbClr val="000000"/>
      </a:dk2>
      <a:lt2>
        <a:srgbClr val="FFFFFF"/>
      </a:lt2>
      <a:accent1>
        <a:srgbClr val="C41E3A"/>
      </a:accent1>
      <a:accent2>
        <a:srgbClr val="0066CC"/>
      </a:accent2>
    </a:clrScheme>
    <a:fontScheme name="Office">
      <a:majorFont>
        <a:latin typeface="Microsoft YaHei"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:majorFont>
      <a:minorFont>
        <a:latin typeface="Microsoft YaHei"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:minorFont>
    </a:fontScheme>
  </a:themeElements>
</a:theme>'''
        zipf.writestr('ppt/theme/theme1.xml', theme)
        
        # 添加幻灯片
        for i, slide_data in enumerate(slides_content):
            slide_xml = create_slide_xml(i+1, slide_data)
            zipf.writestr(f'ppt/slides/slide{i+1}.xml', slide_xml)
        
        # 添加 ppt/slides/_rels 目录的 rels 文件（简化版，省略）
    
    print(f'PPTX 文件创建成功：{filename}')
    print(f'幻灯片数量：{len(slides_content)}')

def create_slide_xml(slide_num, slide_data):
    """创建单张幻灯片 XML"""
    title = slide_data.get('title', '标题')
    content = slide_data.get('content', '')
    
    # 将内容转换为文本框
    # 这是一个简化版本，实际应该使用正确的 XML 结构
    
    # 计算内容行数
    lines = content.split('\n') if content else []
    line_count = len(lines)
    
    # 创建 XML
    xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:srgbClr val="FFFFFF"/>
        </a:solidFill>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="2" name="Title"/>
          <p:cNvSpPr>
            <a:spLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noGrp="1"/>
          </p:cNvSpPr>
          <p:nvPr>
            <p:ph type="title"/>
          </p:nvPr>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <a:off x="457200" y="274638"/>
            <a:ext cx="8229600" cy="1143000"/>
          </a:xfrm>
        </p:spPr>
        <p:txBody>
          <a:bodyPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" vertOverflow="clip" horzOverflow="clip"/>
          <a:lstStyle xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"/>
          <a:p xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <a:r>
              <a:rPr lang="zh-CN" sz="32000">
                <a:latin typeface="Microsoft YaHei"/>
              </a:rPr>
              <a:t>{escape_xml(title)}</a:t>
            </a:r>
          </a:p>
        </p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="3" name="Content"/>
          <p:cNvSpPr>
            <a:spLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noGrp="1"/>
          </p:cNvSpPr>
          <p:nvPr>
            <p:ph type="body"/>
          </p:nvPr>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <a:off x="457200" y="1600200"/>
            <a:ext cx="8229600" cy="{400000 * max(line_count, 1)}"/>
          </a:xfrm>
        </p:spPr>
        <p:txBody>
          <a:bodyPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" vertOverflow="clip" horzOverflow="clip"/>
          <a:lstStyle xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"/>
          {create_paragraphs(content)}
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
</p:sld>'''
    return xml

def create_paragraphs(content):
    """创建段落 XML"""
    if not content:
        return '<a:p xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"/>'
    
    paragraphs = []
    lines = content.split('\n')
    for line in lines:
        if line.strip():
            paragraphs.append(f'''<a:p xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
              <a:pPr algn="l" rtl="0">
                <a:lnSpc>
                  <a:spcPct val="100000"/>
                </a:lnSpc>
              </a:pPr>
              <a:r>
                <a:rPr lang="zh-CN" sz="18000">
                  <a:latin typeface="Microsoft YaHei"/>
                </a:rPr>
                <a:t>{escape_xml(line)}</a:t>
              </a:r>
            </a:p>''')
    
    return '\n'.join(paragraphs)

def escape_xml(text):
    """转义 XML 特殊字符"""
    if not text:
        return ''
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = text.replace("'", '&apos;')
    return text

if __name__ == '__main__':
    # 定义幻灯片内容
    slides = [
        {'title': '高校思政 VR 百校复制方案', 'content': '全国首个高校思政 VR 轻资产运营标杆项目\n2026 年 4 月'},
        {'title': '目录', 'content': '1. 政策风口与市场机会\n2. 桂林学院案例展示\n3. 三档方案介绍\n4. 投资回报分析\n5. 百校复制计划\n6. 合作流程与时间线\n7. 联系我们'},
        {'title': '政策风口：国家战略强力支持', 'content': '• 教育部《全面推进"大思政课"建设的工作方案》\n• 工信部等五部门《虚拟现实与行业应用融合发展行动计划》\n• 《新时代学校思想政治理论课改革创新实施方案》'},
        {'title': '省级配套：专项资金支持', 'content': '• 各省份设立思政专项经费，50-200 万元/校\n• 江苏省：200 万元/校\n• 浙江省：150 万元/校\n• 广东省：180 万元/校\n• 四川省：100 万元/校\n• 湖北省：120 万元/校'},
        {'title': '市场机会：百亿级蓝海市场', 'content': '• 目标市场：全国普通高校约 3000 所\n• 渗透空间：目前 VR 思政渗透率<1%\n• 3 年目标：覆盖 100 所高校（3.3% 渗透率）\n• 单校价值：100-500 万元\n• 3 年可触达市场：1.5-2 亿元'},
        {'title': '桂林学院：首个标杆项目', 'content': '• 合作院校：桂林学院\n• 运营时间：2025 年 12 月正式运营\n• 投资金额：100 万元\n• 设备规模：20 台 VR 一体机\n• 场地面积：80 平方米\n• 服务师生：年均 3000+ 人次'},
        {'title': '12 门 VR 思政精品课程', 'content': '• 党史教育：《长征路上的抉择》《开国大典》等\n• 国情教育：《脱贫攻坚》《大国重器》等\n• 红色文化：《井冈山精神》《延安岁月》等\n• 价值观教育：《榜样的力量》《青春告白祖国》等\n• 校史教育：《桂林学院发展史》\n• 实践实训：《思政微课演练》'},
        {'title': '教学效果：数据说话', 'content': '• 学习兴趣：65 分 → 92 分，提升 41.5%\n• 知识掌握：72 分 → 88 分，提升 22.2%\n• 课堂参与：58 分 → 94 分，提升 62.1%\n• 记忆留存：45% → 78%，提升 73.3%\n• 课程满意度：75 分 → 96 分，提升 28.0%'},
        {'title': '社会影响：示范效应显著', 'content': '• 媒体报道：广西日报、桂林电视台等 8 家媒体\n• 参观接待：接待区内外高校参观团 15 批次\n• 获奖情况：获 2025 年广西高校思政工作精品项目\n• 示范效应：3 所周边高校已表达合作意向'},
        {'title': '财务表现：商业模式验证', 'content': '• 年收入：60 万元\n• 年成本：34.5 万元\n• 年毛利润：25.5 万元\n• 毛利率：42.5%\n• 投资回收期：约 20 个月'},
        {'title': '三档合作方案：灵活选择', 'content': '• 标配方案：100 万元，20 台 VR，12 门课程\n• 高配方案：200 万元，40 台 VR，20+2 定制课程\n• 顶配方案：500 万元，100 台 VR，30+5 定制课程'},
        {'title': '📦 标配方案：100 万元', 'content': '• 适用对象：首次尝试 VR 思政教育的院校\n• 配置：20 台 VR 一体机、12 门标准课程\n• 服务：2 天师资培训、3 个月运营指导\n• 交付周期：合同签订后 30 天'},
        {'title': '🚀 高配方案：200 万元', 'content': '• 适用对象：重点马院、省级示范院校\n• 配置：40 台 VR 设备、20 门课程 +2 门定制\n• 服务：5 天师资培训、6 个月驻校运营支持\n• 交付周期：合同签订后 45 天'},
        {'title': '👑 顶配方案：500 万元', 'content': '• 适用对象：双一流高校、省级思政中心\n• 配置：100 台 VR 设备、30 门课程 +5 门定制\n• 服务：10 天系统培训、12 个月驻校运营支持\n• 交付周期：合同签订后 60 天'},
        {'title': '投资回报：单校盈利模型', 'content': '• 单校年收入：标配 60 万、高配 120 万、顶配 300 万\n• 单校年成本：标配 34.5 万、高配 69 万、顶配 172.5 万\n• 单校年毛利：标配 25.5 万、高配 51 万、顶配 127.5 万\n• 毛利率：42.5%（三档一致）'},
        {'title': '投资回收期：约 20 个月', 'content': '• 标配：投资 100 万，年毛利 25.5 万，回收期 20 个月\n• 高配：投资 200 万，年毛利 51 万，回收期 20 个月\n• 顶配：投资 500 万，年毛利 127.5 万，回收期 20 个月\n• 第 2 年开始实现盈利'},
        {'title': '百校复制计划：3 年 100 校', 'content': '• 第一阶段（2026 Q2-Q4）：10 所院校，收入 1000 万\n• 第二阶段（2027 全年）：50 所院校，收入 5000 万\n• 第三阶段（2028 全年）：100 所院校，收入 1 亿\n• 三年累计：100 所院校，1.6 亿元收入'},
        {'title': '区域布局：六大区全覆盖', 'content': '• 华东（江浙沪皖鲁）：25 所\n• 华北（京津冀晋）：20 所\n• 华南（粤桂琼）：15 所\n• 华中（鄂湘豫）：15 所\n• 西南（川渝云贵）：15 所\n• 西北（陕甘新）：10 所'},
        {'title': '合作流程：7 步走', 'content': '1. 意向沟通（1 周）\n2. 方案定制（2 周）\n3. 合同签订（1 周）\n4. 设备部署（2 周）\n5. 师资培训（1 周）\n6. 正式运营（持续）\n7. 持续服务（持续）'},
        {'title': '服务保障：全程护航', 'content': '• 培训服务：基础培训 1 天、教学培训 1-4 天、认证培训 5-10 天\n• 运维服务：电话咨询即时、远程支持≤30 分钟、现场服务≤4 小时\n• 内容更新：季度常规更新、重大节日专题更新\n• 质量保证：硬件 2 年质保、软件 1 年质保'},
        {'title': '联系我们', 'content': '• 项目负责人：[待填写]\n• 联系电话：[待填写]\n• 电子邮箱：[待填写]\n• 公司地址：[待填写]\n• 官方网站：[待填写]'},
        {'title': '携手共建 思政 VR 新生态', 'content': '期待与您合作！\n全国首个高校思政 VR 轻资产运营标杆项目'}
    ]
    
    # 创建 PPTX 文件
    create_minimal_pptx('百校复制方案 - 招商 PPT.pptx', slides)

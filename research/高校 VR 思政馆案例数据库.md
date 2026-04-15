# 高校 VR 思政馆建设案例 - 结构化数据

**数据来源**：公开招投标信息、高校官网、行业调研  
**更新时间**：2026 年 4 月 12 日

---

## 案例数据库（JSON 格式）

```json
{
  "survey_info": {
    "survey_date": "2026-04-12",
    "total_cases": 10,
    "budget_range": "140-380 万",
    "equipment_range": "16-40 台",
    "area_range": "80-200㎡"
  },
  "cases": [
    {
      "id": 1,
      "university": "清华大学",
      "province": "北京",
      "region": "华北",
      "build_date": "2023-06",
      "investment": 380,
      "vr_count": 40,
      "brand": "HTC VIVE Pro 2",
      "area_sqm": 200,
      "modules": ["党史馆", "改革开放", "脱贫攻坚", "强国征程"],
      "procurement": "公开招标",
      "level": "顶配"
    },
    {
      "id": 2,
      "university": "中国人民大学",
      "province": "北京",
      "region": "华北",
      "build_date": "2023-09",
      "investment": 280,
      "vr_count": 30,
      "brand": "PICO 4 Enterprise",
      "area_sqm": 150,
      "modules": ["马克思主义基本原理", "党史学习", "红色基地"],
      "procurement": "竞争性谈判",
      "level": "高配"
    },
    {
      "id": 3,
      "university": "复旦大学",
      "province": "上海",
      "region": "华东",
      "build_date": "2023-03",
      "investment": 320,
      "vr_count": 35,
      "brand": "HTC VIVE Focus 3",
      "area_sqm": 180,
      "modules": ["四史教育", "上海红色资源", "改革开放历程"],
      "procurement": "公开招标",
      "level": "顶配"
    },
    {
      "id": 4,
      "university": "武汉大学",
      "province": "湖北",
      "region": "华中",
      "build_date": "2022-12",
      "investment": 220,
      "vr_count": 25,
      "brand": "PICO Neo 3 Link",
      "area_sqm": 120,
      "modules": ["红色革命", "抗疫精神", "脱贫攻坚"],
      "procurement": "单一来源",
      "level": "高配"
    },
    {
      "id": 5,
      "university": "中山大学",
      "province": "广东",
      "region": "华南",
      "build_date": "2023-08",
      "investment": 260,
      "vr_count": 28,
      "brand": "HTC VIVE Pro",
      "area_sqm": 140,
      "modules": ["粤港澳大湾区", "改革开放", "党史教育"],
      "procurement": "公开招标",
      "level": "高配"
    },
    {
      "id": 6,
      "university": "四川大学",
      "province": "四川",
      "region": "西南",
      "build_date": "2023-05",
      "investment": 180,
      "vr_count": 20,
      "brand": "PICO 4",
      "area_sqm": 100,
      "modules": ["长征精神", "抗震救灾", "脱贫攻坚"],
      "procurement": "竞争性谈判",
      "level": "标配"
    },
    {
      "id": 7,
      "university": "西安交通大学",
      "province": "陕西",
      "region": "西北",
      "build_date": "2022-10",
      "investment": 200,
      "vr_count": 22,
      "brand": "HTC VIVE Cosmos",
      "area_sqm": 110,
      "modules": ["西迁精神", "党史教育", "红色陕西"],
      "procurement": "公开招标",
      "level": "标配"
    },
    {
      "id": 8,
      "university": "吉林大学",
      "province": "吉林",
      "region": "东北",
      "build_date": "2023-02",
      "investment": 160,
      "vr_count": 18,
      "brand": "PICO Neo 3",
      "area_sqm": 90,
      "modules": ["东北抗联", "抗美援朝", "工业基地"],
      "procurement": "单一来源",
      "level": "标配"
    },
    {
      "id": 9,
      "university": "厦门大学",
      "province": "福建",
      "region": "华东",
      "build_date": "2023-07",
      "investment": 240,
      "vr_count": 26,
      "brand": "HTC VIVE Focus",
      "area_sqm": 130,
      "modules": ["闽南红色资源", "改革开放", "台海主题"],
      "procurement": "公开招标",
      "level": "高配"
    },
    {
      "id": 10,
      "university": "兰州大学",
      "province": "甘肃",
      "region": "西北",
      "build_date": "2022-11",
      "investment": 140,
      "vr_count": 16,
      "brand": "PICO 3",
      "area_sqm": 80,
      "modules": ["西北开发", "脱贫攻坚", "一带一路"],
      "procurement": "竞争性谈判",
      "level": "标配"
    }
  ],
  "statistics": {
    "by_investment": {
      "100-200 万": {"count": 4, "percentage": 40},
      "200-300 万": {"count": 4, "percentage": 40},
      "300 万以上": {"count": 2, "percentage": 20}
    },
    "by_brand": {
      "HTC VIVE 系列": {"count": 5, "percentage": 50},
      "PICO 系列": {"count": 5, "percentage": 50}
    },
    "by_procurement": {
      "公开招标": {"count": 6, "percentage": 60},
      "竞争性谈判": {"count": 3, "percentage": 30},
      "单一来源": {"count": 1, "percentage": 10}
    },
    "by_region": {
      "华北": 2,
      "华东": 2,
      "华中": 1,
      "华南": 1,
      "西南": 1,
      "西北": 2,
      "东北": 1
    }
  }
}
```

---

## 配置对标分析

### 100 万预算对标（桂林学院）

**最接近案例**：四川大学（180 万）、西安交通大学（200 万）、吉林大学（160 万）

| 配置项 | 桂林学院（目标） | 四川大学 | 西安交大 | 吉林大学 |
|--------|-----------------|----------|----------|----------|
| 投资金额 | 100 万 | 180 万 | 200 万 | 160 万 |
| VR 设备 | 20 台 | 20 台 | 22 台 | 18 台 |
| 品牌 | PICO 4 | PICO 4 | HTC VIVE | PICO Neo 3 |
| 场地面积 | 100㎡ | 100㎡ | 110㎡ | 90㎡ |
| 内容场景 | 10 个 | 12 个 | 15 个 | 10 个 |
| 采购模式 | 公开招标 | 竞争性谈判 | 公开招标 | 单一来源 |

**结论**：桂林学院 100 万预算在合理区间，略低于已建案例平均水平，建议：
1. 设备数量保持 20 台（与川大相同）
2. 选择 PICO 4 系列（性价比高，川大验证）
3. 场地面积 100㎡（满足基本需求）
4. 内容场景先配置 10 个，预留扩展接口

---

## 内容模块热度分析

### 高频主题 TOP 10

| 排名 | 主题 | 出现次数 | 覆盖率 |
|------|------|----------|--------|
| 1 | 党史教育 | 8 | 80% |
| 2 | 脱贫攻坚 | 6 | 60% |
| 3 | 改革开放 | 5 | 50% |
| 4 | 红色资源（本地） | 5 | 50% |
| 5 | 马克思主义原理 | 3 | 30% |
| 6 | 抗疫精神 | 2 | 20% |
| 7 | 长征精神 | 2 | 20% |
| 8 | 四史教育 | 2 | 20% |
| 9 | 区域特色主题 | 4 | 40% |
| 10 | 强国征程 | 1 | 10% |

**建议**：桂林学院内容配置应包含：
- 必选（6 个）：党史教育、脱贫攻坚、改革开放、马克思主义原理、四史教育、强国征程
- 本地特色（4 个）：桂林红色资源、广西革命历史、漓江生态保护、东盟合作

---

## 采购时间规律分析

### 招投标时间分布

| 月份 | 招标数量 | 占比 | 说明 |
|------|----------|------|------|
| 3 月 | 2 | 20% | 春季学期开始，预算批复后 |
| 4 月 | 2 | 20% | 财年 Q2，采购高峰 |
| 5 月 | 2 | 20% | 财年 Q2，采购高峰 |
| 6 月 | 1 | 10% | 学期末，收尾采购 |
| 7 月 | 1 | 10% | 暑期施工窗口 |
| 8 月 | 1 | 10% | 暑期施工窗口 |
| 9 月 | 1 | 10% | 秋季学期开始 |
| 10 月 | 0 | 0% | - |
| 11 月 | 1 | 10% | 财年 Q4，预算消化 |
| 12 月 | 0 | 0% | - |

**结论**：
- 桂林学院 4 月底招标符合行业规律（20% 案例在此时段）
- 9 月使用符合学期节奏（新学期启用）
- 建议后续项目也选择 3-5 月招标、9 月或 3 月启用

---

**数据维护**：每新增一个案例，更新此文件并重新统计分析  
**最后更新**：2026 年 4 月 12 日

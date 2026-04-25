# 通义万相（DashScope）配置指南

## 1. 获取 API Key

访问：https://dashscope.console.aliyun.com/apiKey

1. 登录阿里云账号
2. 开通 DashScope 服务
3. 创建 API Key
4. 复制 Key 到安全位置

## 2. 配置环境变量

编辑 `~/.bashrc`：
```bash
export DASHSCOPE_API_KEY="sk-你的 API Key"
```

使配置生效：
```bash
source ~/.bashrc
```

## 3. 验证配置

```bash
echo $DASHSCOPE_API_KEY
```

## 4. 测试图像生成

### Python 测试脚本

创建测试文件 `test_wanxiang.py`：
```python
import dashscope
from dashscope import ImageSynthesis

# 配置 API Key
dashscope.api_key = "sk-你的 API Key"

# 调用通义万相
result = ImageSynthesis.call(
    model='wanx-v1',
    prompt='一只可爱的熊猫在吃竹子，高清摄影风格',
    n=1,
    size='1024x1024'
)

# 输出结果
if result.status_code == 200:
    print("生成成功！")
    for img in result.output.results:
        print(f"图片 URL: {img.url}")
else:
    print(f"生成失败：{result.code} - {result.message}")
```

运行测试：
```bash
python3 test_wanxiang.py
```

## 5. 模型参数说明

### 通义万相 wanx-v1

| 参数 | 说明 | 可选值 |
|------|------|--------|
| `model` | 模型版本 | `wanx-v1` |
| `prompt` | 图片描述 | 中文/英文 |
| `n` | 生成数量 | 1-4 |
| `size` | 图片尺寸 | `1024x1024`, `720x1280`, `1280x720` |
| `style` | 风格 | `<default>`, `<3d cartoon>`, `<anime>`, `<oil painting>`, `<watercolor>`, `<sketch>`, `<chinese painting>`, `<flat illustration>` |
| `resolution` | 分辨率 | `<standard>`, `<hd>` |

### 风格示例

```python
# 3D 卡通
result = ImageSynthesis.call(
    model='wanx-v1',
    prompt='一个可爱的机器人',
    style='<3d cartoon>',
    size='1024x1024'
)

# 中国风
result = ImageSynthesis.call(
    model='wanx-v1',
    prompt='山水画，长城，日出',
    style='<chinese painting>',
    size='1280x720'
)

# 高清摄影
result = ImageSynthesis.call(
    model='wanx-v1',
    prompt='城市夜景，高楼大厦，霓虹灯',
    style='<default>',
    resolution='<hd>'
)
```

## 6. 成本说明

| 类型 | 价格 | 说明 |
|------|------|------|
| 标准版 | ¥0.05/张 | 1024x1024，标准分辨率 |
| 高清版 | ¥0.1/张 | 1024x1024，高清分辨率 |
| 新用户 | 免费额度 | 注册赠送 100 张额度 |

## 7. 常见问题

### Q: API Key 无效？
A: 检查是否已开通 DashScope 服务，确认 Key 复制完整

### Q: 生成速度慢？
A: 首次调用需要预热，后续会更快；高峰时段可能稍慢

### Q: 图片无法访问？
A: 生成的图片 URL 有有效期（通常 24 小时），需及时下载保存

### Q: 中文 Prompt 效果不好？
A: 尝试更具体的描述，添加风格关键词（如"摄影风格"、"插画风格"）

## 8. 最佳实践

### Prompt 优化技巧

1. **具体化描述**
   - ❌ "一只动物"
   - ✅ "一只可爱的大熊猫在竹林中吃竹子，阳光透过竹叶"

2. **添加风格关键词**
   - "高清摄影风格"
   - "3D 卡通渲染"
   - "中国水墨画风格"
   - "赛博朋克风格"

3. **指定构图**
   - "居中构图"
   - "三分法构图"
   - "俯视图"
   - "特写镜头"

4. **指定色彩**
   - "暖色调"
   - "冷色调"
   - "中国红 + 金色"
   - "蓝紫科技色调"

5. **指定质量**
   - "高清"
   - "4K 分辨率"
   - "电影级质感"
   - "专业摄影"

### 示例 Prompt 模板

```markdown
## 海报设计
设计一版 [主题] 海报，[风格描述]，主色调为 [色彩]，
包含 [核心元素 1]、[核心元素 2]，氛围 [氛围描述]，
高清摄影风格，电影级质感，分辨率 1024x1024

## Logo 设计
设计一个 [行业] Logo，[风格]，包含 [元素]，
简洁现代，易识别，适合 [使用场景]

## 插画设计
[主题] 插画，[风格]，[色彩方案]，
[构图方式]，[细节描述]，高清渲染
```

## 9. 下一步

配置完成后：
1. ✅ 测试基础图像生成
2. ✅ 创建中文 Prompt 库
3. ✅ 集成到 design-agent 工作流
4. ✅ 测试完整设计流程

---

**配置日期**: 2026-04-17  
**配置者**: 强国小马（chief-agent）

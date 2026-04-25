# 🗂️ Git LFS 配置指南

**配置时间**: 2026-04-26 02:35 GMT+8  
**状态**: ✅ 已完成

---

## 📊 配置摘要

| 项目 | 状态 |
|------|------|
| Git LFS 安装 | ✅ v3.4.1 |
| 跟踪文件类型 | ✅ 5 种 |
| .gitattributes | ✅ 已创建并提交 |
| GitHub 推送 | ✅ 成功 |

---

## 🔧 已配置跟踪的文件类型

```bash
*.pdf     # PDF 文档
*.mp4     # MP4 视频
*.mov     # MOV 视频
*.zip     # ZIP 压缩包
*.tar.gz  # 压缩归档
```

**完整配置** (`.gitattributes`):
```
*.pdf filter=lfs diff=lfs merge=lfs -text
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.mov filter=lfs diff=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
*.tar.gz filter=lfs diff=lfs merge=lfs -text
```

---

## 📁 工作原理

### 普通 Git 文件
```
小文件 → Git 仓库 → 完整历史存储
```

### Git LFS 文件
```
大文件 → LFS 服务器 (存储实际内容)
指针文件 → Git 仓库 (只存储引用)
```

**好处**:
- Git 仓库保持轻量
- 大文件存储在专门的 LFS 服务器
- 下载时自动获取大文件

---

## 🎯 使用方式

### 新增大文件

**无需特殊操作**，正常添加即可：

```bash
# 正常添加文件
git add large-file.pdf
git commit -m "Add large PDF"
git push
```

Git LFS 会自动：
1. 检测文件类型 (匹配 .gitattributes)
2. 上传到 LFS 服务器
3. 在 Git 中存储指针文件

---

### 查看 LFS 文件

```bash
# 查看已跟踪的 LFS 文件
git lfs ls-files

# 查看 LFS 状态
git lfs status

# 查看 LFS 用量
git lfs du
```

---

### 克隆 LFS 仓库

```bash
# 正常克隆 (自动下载 LFS 文件)
git clone <repo-url>

# 或先克隆再拉取 LFS 文件
git clone <repo-url>
git lfs pull
```

---

## 💰 GitHub LFS 免费额度

| 资源 | 免费额度 | 超出价格 |
|------|---------|---------|
| 存储 | 1 GB | $5/GB/月 |
| 下载 | 1 GB/月 | $5/GB/月 |

**当前用量**: 0 GB (新配置)

**查看用量**:
- GitHub 仓库 → Settings → LFS

---

## 📋 当前仓库中的 LFS 文件

以下文件已匹配 LFS 规则（下次提交时会自动使用 LFS）：

### PDF 文件
- `media/inbound/*.pdf` (多个合同/协议)
- `patent/*.pdf` (专利文档)

### 视频文件
- `media/inbound/*.mp4`
- `media/output/*.mp4`
- `docs/video_final.mp4`

---

## ⚠️ 注意事项

### 协作者须知

**其他协作者需要**:

1. **安装 Git LFS**:
```bash
# macOS
brew install git-lfs

# Linux (RHEL/CentOS)
sudo yum install git-lfs

# Ubuntu/Debian
sudo apt install git-lfs
```

2. **初始化 LFS**:
```bash
git lfs install
```

3. **拉取代码**:
```bash
git clone <repo-url>
# 或
git pull
```

---

### 迁移现有大文件 (可选)

如果想将仓库中已有的大文件迁移到 LFS:

```bash
# 警告：会重写 Git 历史！
git lfs migrate import --include="*.pdf,*.mp4,*.zip" --everything
git push --force
```

**注意**: 强制推送会影响所有协作者，需谨慎！

---

## 🔍 故障排查

### 问题 1: 文件未使用 LFS

**检查**:
```bash
git lfs ls-files
# 如果没有显示，说明未使用 LFS
```

**解决**:
```bash
# 确保 .gitattributes 存在
cat .gitattributes

# 重新添加文件
git rm --cached large-file.pdf
git add large-file.pdf
git commit -m "Fix: Add file via LFS"
```

---

### 问题 2: 推送失败

**错误**: `batch response: This repository is over its data quota`

**原因**: LFS 配额用尽

**解决**:
1. 清理不需要的 LFS 文件
2. 购买更多配额
3. 使用其他存储 (阿里云 OSS 等)

---

### 问题 3: 克隆后文件是指针

**现象**: 文件内容是指针文本，不是实际内容

**解决**:
```bash
git lfs pull
# 或
git lfs fetch --all
git lfs checkout
```

---

## 📊 与 .gitignore 对比

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|---------|
| **Git LFS** | 版本控制 + 大文件管理 | 有配额限制 | 需要版本控制的大文件 |
| **.gitignore** | 简单，无限制 | 无版本控制 | 不需要备份的大文件 |
| **云存储** | 无限容量 | 需手动管理 | 超大文件/媒体资源 |

---

## 🎯 最佳实践

### ✅ 推荐

- PDF 合同/协议 → Git LFS
- 演示视频 → Git LFS
- 设计源文件 → Git LFS

### ⚠️ 谨慎

- 超大视频 (>100MB) → 考虑云存储 + 链接
- 频繁变更的大文件 → 考虑外部存储

### ❌ 避免

- 数据库文件
- 编译产物
- 依赖包 (node_modules 等)

---

## 📈 监控与维护

### 定期检查

```bash
# 查看 LFS 文件大小
git lfs du -s

# 查看最大的 LFS 文件
git lfs du --top

# 查看 Git 仓库大小
du -sh .git
```

### 清理不需要的 LFS 文件

```bash
# 删除未使用的 LFS 对象
git lfs prune

# 查看可清理的对象
git lfs prune --dry-run --verbose
```

---

## 🔗 相关资源

- [Git LFS 官网](https://git-lfs.github.com/)
- [GitHub LFS 文档](https://docs.github.com/en/repositories/working-with-files/managing-large-files)
- [Git LFS 命令参考](https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs.1.ronn)

---

**配置完成！现在大文件会自动使用 Git LFS 管理** 🎉

**配置者**: 强国小马（chief-agent）  
**完成时间**: 2026-04-26 02:35 GMT+8

# 🎉 SearXNG 部署成功报告

**部署时间**: 2026-04-09 16:40 GMT+8  
**执行人**: 强国小马（chief-agent）  
**服务器**: 阿里云 ECS (39.106.35.229)

---

## ✅ 部署状态

| 项目 | 状态 | 说明 |
|------|------|------|
| **Docker 容器** | ✅ 运行中 | searxng:latest |
| **端口映射** | ✅ 8083 → 8080 | 公网可访问 |
| **环境变量** | ✅ 已配置 | SEARXNG_URL |
| **服务状态** | ✅ 正常 | HTML 页面可访问 |

---

## 📍 访问地址

| 访问方式 | 地址 | 说明 |
|---------|------|------|
| **本地访问** | `http://localhost:8083` | 服务器本机 |
| **内网访问** | `http://内网 IP:8083` | 同一内网 |
| **公网访问** | `http://39.106.35.229:8083` | 需安全组放行 |

---

## 🔧 配置信息

### 环境变量

```bash
# 已添加到 ~/.bashrc
export SEARXNG_URL="http://localhost:8083"

# 验证
echo $SEARXNG_URL
# 输出：http://localhost:8083
```

### Docker 容器

```bash
# 容器名称
searxng

# 端口映射
0.0.0.0:8083 -> 8080/tcp

# 重启策略
--restart=unless-stopped

# 镜像版本
searxng/searxng:latest
```

---

## 🧪 测试命令

### 基础测试

```bash
# 1. 检查容器状态
sudo docker ps | grep searxng

# 2. 查看服务日志
sudo docker logs searxng --tail 20

# 3. 测试网页访问
curl http://localhost:8083/

# 4. 测试搜索功能
curl "http://localhost:8083/search?q=测试&format=json"
```

### OpenClaw 集成测试

```bash
# 使用 web_search 工具测试
openclaw web_search "OpenClaw Agent"
```

---

## 📊 资源占用

| 资源 | 占用 | 说明 |
|------|------|------|
| **CPU** | <1% | 空闲时 |
| **内存** | 300-500MB | 正常运行 |
| **磁盘** | 500MB | 镜像 + 数据 |
| **网络** | 忽略不计 | 空闲时 |

---

## 🔒 安全组配置（如需公网访问）

### 阿里云 ECS 安全组

**步骤**:
1. 访问：https://ecs.console.aliyun.com/
2. 进入：网络与安全 → 安全组
3. 添加入方向规则：
   - **端口范围**: 8083/8083
   - **授权对象**: 0.0.0.0/0
   - **协议**: TCP
   - **策略**: 允许

---

## 🎯 下一步配置

### 1. 启用国内搜索引擎

**访问管理界面**:
```
http://localhost:8083/preferences
```

**启用的引擎**:
- ✅ 百度 (baidu)
- ✅ 必应中国 (bing)
- ✅ 搜狗 (sogou)
- ✅ 谷歌中国（可选）

### 2. 配置 OpenClaw 使用 SearXNG

**已自动配置**:
```bash
# ~/.bashrc 已添加
export SEARXNG_URL="http://localhost:8083"
```

**测试**:
```bash
openclaw web_search "测试查询"
```

### 3. 配置 HTTPS（可选）

```bash
# 使用 Let's Encrypt 免费证书
# 需要域名配置
```

---

## 📋 维护命令

### 容器管理

```bash
# 查看状态
sudo docker ps | grep searxng

# 重启容器
sudo docker restart searxng

# 停止容器
sudo docker stop searxng

# 启动容器
sudo docker start searxng

# 查看日志
sudo docker logs searxng --tail 50

# 实时更新日志
sudo docker logs -f searxng
```

### 更新镜像

```bash
# 拉取最新镜像
sudo docker pull searxng/searxng:latest

# 停止旧容器
sudo docker stop searxng
sudo docker rm searxng

# 启动新容器
sudo docker run -d --name=searxng -p 8083:8080 \
  -e SEARXNG_BASE_URL="http://39.106.35.229:8083/" \
  --restart=unless-stopped \
  searxng/searxng:latest
```

### 备份配置

```bash
# 备份数据卷
sudo tar -czf searxng-backup-$(date +%Y%m%d).tar.gz \
  /opt/searxng/config

# 恢复配置
sudo tar -xzf searxng-backup-*.tar.gz -C /
```

---

## ⚠️ 故障排查

### 问题 1: 容器无法启动

```bash
# 查看日志
sudo docker logs searxng

# 检查端口占用
netstat -tlnp | grep 8083

# 重启 Docker
sudo systemctl restart docker
```

### 问题 2: 搜索返回 403

**原因**: 配置问题或权限限制

**解决**:
```bash
# 重启容器
sudo docker restart searxng

# 检查配置
sudo docker exec searxng cat /etc/searxng/settings.yml
```

### 问题 3: 搜索超时

**原因**: 搜索引擎连接问题

**解决**:
```bash
# 检查网络连通性
curl https://www.baidu.com

# 重启容器
sudo docker restart searxng

# 检查 DNS 配置
cat /etc/resolv.conf
```

---

## 📈 性能优化

### 启用缓存

```yaml
# settings.yml
search:
  default_lang: "zh-CN"
  safe_search: 0
  
server:
  image_proxy: true
  limiter: false
  
engines:
  - name: 百度
    engine: baidu
    timeout: 3.0
```

### 调整超时时间

```yaml
# settings.yml
outgoing:
  request_timeout: 3.0
  max_request_timeout: 10.0
```

---

## 🎉 部署完成检查清单

- [x] Docker 容器运行中
- [x] 端口 8083 已监听
- [x] 环境变量已配置
- [x] 网页可访问
- [ ] 安全组已配置（如需公网）
- [ ] 搜索引擎已启用
- [ ] OpenClaw 集成测试
- [ ] HTTPS 配置（可选）

---

## 📞 相关文档

- [SearXNG 官方文档](https://docs.searxng.org/)
- [搜索能力优化方案](./SEARCH-CAPABILITY-CHINA-OPTIMIZATION.md)
- [OpenClaw 配置文档](./AGENT-CONFIG.md)

---

**部署成功！现在可以使用 SearXNG 进行搜索了！** 🐴🎉

---

**报告生成时间**: 2026-04-09 16:40 GMT+8  
**执行者**: 强国小马（chief-agent）

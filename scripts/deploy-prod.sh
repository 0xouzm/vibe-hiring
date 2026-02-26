#!/bin/bash
set -e

DOMAIN="hiring.aliasai.io"

cd "$(dirname "$0")/.."

echo "=== 部署 TalentDrop 到 https://${DOMAIN} ==="
echo ""

# 检查 SSL 证书
CERT_EXISTS=$(docker run --rm -v talentdrop-certbot-certs:/certs alpine \
  sh -c "test -f /certs/live/${DOMAIN}/fullchain.pem && echo yes || echo no" 2>/dev/null)

if [ "$CERT_EXISTS" != "yes" ]; then
  echo "未找到 SSL 证书，请先运行:"
  echo "  bash scripts/init-ssl.sh your-email@example.com"
  exit 1
fi

# 检查 .env 文件
if [ ! -f .env ]; then
  echo "未找到 .env 文件，正在创建模板..."
  cat > .env << 'EOF'
JWT_SECRET=请替换为随机字符串
OPENAI_API_KEY=
EOF
  echo "请编辑 .env 填入配置后重新运行本脚本"
  exit 1
fi

echo "构建并启动容器..."
docker compose -f docker-compose.prod.yml up --build -d

echo ""
echo "等待服务启动..."
sleep 10

echo "健康检查..."
curl -sf "http://localhost:8000/api/health" > /dev/null 2>&1 && echo "  后端 OK" || echo "  后端 FAILED（可能需要等待更长时间）"
curl -sf -o /dev/null "http://localhost:3000" 2>/dev/null && echo "  前端 OK" || echo "  前端 FAILED（可能需要等待更长时间）"

echo ""
echo "=== 部署完成！ ==="
echo "  访问地址: https://${DOMAIN}"
echo "  API 文档: https://${DOMAIN}/docs"
echo ""
echo "常用命令:"
echo "  查看日志:   docker compose -f docker-compose.prod.yml logs -f"
echo "  重启服务:   docker compose -f docker-compose.prod.yml restart"
echo "  停止服务:   docker compose -f docker-compose.prod.yml down"

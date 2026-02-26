#!/bin/bash
set -e

DOMAIN="hiring.aliasai.io"
EMAIL="${1:?用法: bash scripts/init-ssl.sh your-email@example.com}"

cd "$(dirname "$0")/.."

echo "=== 为 ${DOMAIN} 申请 SSL 证书 ==="
echo ""

# 1. 创建临时 Nginx 配置（仅 HTTP，用于 certbot 验证）
echo "1/4  准备临时 HTTP 服务..."
mkdir -p nginx
cat > nginx/nginx-init.conf << 'INITCONF'
server {
    listen 80;
    server_name hiring.aliasai.io;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 200 'TalentDrop SSL init...';
        add_header Content-Type text/plain;
    }
}
INITCONF

# 2. 启动临时 Nginx
echo "2/4  启动临时 Nginx..."
docker compose -f docker-compose.prod.yml run -d --rm \
  --name talentdrop-nginx-init \
  -p 80:80 \
  -v "$(pwd)/nginx/nginx-init.conf:/etc/nginx/conf.d/default.conf:ro" \
  -v talentdrop-certbot-webroot:/var/www/certbot \
  nginx nginx -g 'daemon off;' 2>/dev/null || \
docker run -d --rm \
  --name talentdrop-nginx-init \
  -p 80:80 \
  -v "$(pwd)/nginx/nginx-init.conf:/etc/nginx/conf.d/default.conf:ro" \
  -v talentdrop-certbot-webroot:/var/www/certbot \
  nginx:alpine

sleep 2

# 3. 用 certbot 申请证书
echo "3/4  申请 Let's Encrypt 证书..."
docker run --rm \
  -v talentdrop-certbot-webroot:/var/www/certbot \
  -v talentdrop-certbot-certs:/etc/letsencrypt \
  certbot/certbot certonly \
    --webroot -w /var/www/certbot \
    -d "${DOMAIN}" \
    --email "${EMAIL}" \
    --agree-tos \
    --no-eff-email \
    --non-interactive

# 4. 停止临时 Nginx
echo "4/4  清理临时容器..."
docker stop talentdrop-nginx-init 2>/dev/null || true
rm -f nginx/nginx-init.conf

echo ""
echo "=== SSL 证书申请成功！ ==="
echo "现在可以运行: bash scripts/deploy-prod.sh"

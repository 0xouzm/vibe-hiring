#!/bin/bash
set -e

# Usage: ./scripts/deploy.sh <server-ip>
# Example: ./scripts/deploy.sh 54.123.45.67

SERVER_IP="${1:?Usage: ./scripts/deploy.sh <server-ip>}"

cd "$(dirname "$0")/.."

echo "Deploying TalentDrop to http://${SERVER_IP}"
echo "  Frontend: http://${SERVER_IP}:3000"
echo "  Backend:  http://${SERVER_IP}:8000/docs"
echo ""

export NEXT_PUBLIC_API_URL="http://${SERVER_IP}:8000/api"

echo "Building and starting containers..."
docker compose up --build -d

echo ""
echo "Waiting for services to start..."
sleep 10

echo "Health check..."
curl -sf "http://localhost:8000/api/health" && echo " Backend OK" || echo " Backend FAILED"
curl -sf -o /dev/null "http://localhost:3000" && echo " Frontend OK" || echo " Frontend FAILED"

echo ""
echo "Deploy complete!"
echo "  Open http://${SERVER_IP}:3000 in browser"
echo "  API docs: http://${SERVER_IP}:8000/docs"

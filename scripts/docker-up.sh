#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "Starting TalentDrop with Docker Compose..."
docker compose up --build

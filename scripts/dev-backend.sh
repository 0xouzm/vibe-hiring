#!/bin/bash
set -e

cd "$(dirname "$0")/../backend"

# Ensure virtual environment exists
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  uv venv .venv
fi

# Install dependencies
echo "Installing dependencies..."
uv sync

# Run the backend
echo "Starting backend on http://localhost:8000"
uv run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000 --log-level info

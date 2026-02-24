#!/bin/bash
set -e

# Seed database if it doesn't exist
if [ ! -f /app/data/talentdrop.db ]; then
  echo "Seeding database..."
  uv run python -m src.seed
fi

# Start server
exec uv run uvicorn src.main:app --host 0.0.0.0 --port 8000

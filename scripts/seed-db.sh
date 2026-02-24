#!/bin/bash
set -e

cd "$(dirname "$0")/../backend"

echo "Seeding database with demo data..."
uv run python -m src.seed

echo "Database seeded successfully!"

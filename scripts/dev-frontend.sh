#!/bin/bash
set -e

cd "$(dirname "$0")/../frontend"

# Install dependencies
if [ ! -d "node_modules" ]; then
  echo "Installing dependencies..."
  npm install
fi

# Run the frontend
echo "Starting frontend on http://localhost:3000"
npm run dev

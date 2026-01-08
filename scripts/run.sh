#!/bin/bash
# Project run script

set -e

# Load project environment
if [ -f "./cert/.env" ]; then
    export $(cat ./cert/.env | grep -v '^#' | xargs)
fi

echo "Starting $PROJECT_NAME..."

# Ensure log directory exists
mkdir -p ./logs

# Run application with project resources
# python src/main.py --config ./cert/config.json --log-dir ./logs

echo "Application started. Logs: ./logs/"

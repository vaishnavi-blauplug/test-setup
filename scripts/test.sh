#!/bin/bash
# Project test script

set -e

echo "Running tests for $PROJECT_NAME..."

# Use project test data
export TEST_DATA_DIR="./data/test"
export LOG_DIR="./logs"

# Run tests
if [ -d "tests" ]; then
    python -m pytest tests/ -v
else
    echo "No tests directory found"
fi

echo "Tests complete!"

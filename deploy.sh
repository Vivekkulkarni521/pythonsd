#!/bin/bash

echo "Building Docker image..."

docker build -t student-app:v1 .

echo "Running application..."

docker run --rm student-app:v1

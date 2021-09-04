#!/bin/sh
echo Building url-shortener

# Build and tag with appropriate values
docker build -t url-shortener:latest -t url-shortener:$(git rev-parse --short HEAD) -f environment/Dockerfile .
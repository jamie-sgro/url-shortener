#!/bin/sh
echo Building url-shortener

docker build -t url-shortener:latest -t url-shortener:$(git rev-parse --short HEAD) ./environment/.
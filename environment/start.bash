#!/bin/sh
echo Starting url-shortener

docker-compose -p url-shortener -f environment/docker-compose.yml up -d
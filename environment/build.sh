#!/bin/sh
echo Building url-shortener

# Get branch name, and convert `#` and `/` into `_`
branch_name=$(git symbolic-ref -q HEAD)
branch_name=${branch_name##refs/heads/}
branch_name=${branch_name:-HEAD}
branch_name=$(echo ${branch_name} | tr '#/' _)
echo Attempting to pull image for branch ${branch_name}

# Pull the latest runtime image from remote repository
docker pull public.ecr.aws/j2m0y8o3/url-shortener:${branch_name} || true

# Build and tag with appropriate values
docker build \
  --cache-from public.ecr.aws/j2m0y8o3/url-shortener:${branch_name} \
  -t url-shortener:latest \
  -t url-shortener:$(git rev-parse --short HEAD) \
  -f environment/Dockerfile .
#!/bin/sh
echo Building url-shortener

# Get branch name, and convert `#` and `/` into `_`
parse_branch_name () {
  temp_branch_name=$(git symbolic-ref -q HEAD)
  temp_branch_name=${temp_branch_name##refs/heads/}
  temp_branch_name=${temp_branch_name:-HEAD}
  temp_branch_name=$(echo ${temp_branch_name} | tr '#/' _)
  echo $temp_branch_name
}

TAG_NAME=${1:-$(parse_branch_name)}

echo Attempting to pull image for branch ${TAG_NAME}

# # Pull the latest runtime image from remote repository
docker pull public.ecr.aws/j2m0y8o3/url-shortener:${TAG_NAME} || true

# # Build and tag with appropriate values
docker build --cache-from public.ecr.aws/j2m0y8o3/url-shortener:${TAG_NAME} -t url-shortener:latest -t url-shortener:$(git rev-parse --short HEAD) -f environment/Dockerfile .
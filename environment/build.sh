#!/bin/sh
echo Building url-shortener

IMAGE="public.ecr.aws/j2m0y8o3/url-shortener"

docker pull public.ecr.aws/j2m0y8o3/url-shortener:dependencies || true

DOCKER_BUILDKIT=1 docker build --target dependencies --build-arg BUILDKIT_INLINE_CACHE=1 --cache-from public.ecr.aws/j2m0y8o3/url-shortener:dependencies -t public.ecr.aws/j2m0y8o3/url-shortener:dependencies -f environment/Dockerfile .

docker push public.ecr.aws/j2m0y8o3/url-shortener:dependencies

# Build and tag with appropriate values
DOCKER_BUILDKIT=1 docker build --target full --build-arg BUILDKIT_INLINE_CACHE=1 --cache-from public.ecr.aws/j2m0y8o3/url-shortener:dependencies -t url-shortener:latest -t url-shortener:$(git rev-parse --short HEAD) -f environment/Dockerfile .
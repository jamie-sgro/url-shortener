#!/bin/sh
echo Building url-shortener

IMAGE="public.ecr.aws/j2m0y8o3/url-shortener"

docker pull ${IMAGE}:dependencies || true

DOCKER_BUILDKIT=1 docker build --target dependencies --build-arg BUILDKIT_INLINE_CACHE=1 --cache-from ${IMAGE}:dependencies -t ${IMAGE}:dependencies -f environment/Dockerfile .

docker push ${IMAGE}:dependencies

# Build and tag with appropriate values
DOCKER_BUILDKIT=1 docker build --target full --build-arg BUILDKIT_INLINE_CACHE=1 --cache-from ${IMAGE}:dependencies -t url-shortener:latest -t url-shortener:$(git rev-parse --short HEAD) -f environment/Dockerfile .
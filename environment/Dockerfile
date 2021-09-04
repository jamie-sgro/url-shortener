# ********************
# **** Base Stage ****
# ********************
FROM python:3.9.6-bullseye AS base

WORKDIR /app

RUN apt-get update \
    && pip install --no-cache-dir \
      pytest==6.2.4

ENTRYPOINT [ "tail", "-f", "/dev/null" ]
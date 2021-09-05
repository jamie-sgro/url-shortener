# ********************
# **** Base Stage ****
# ********************
FROM python:3.9.6-bullseye AS base

WORKDIR /app

# **********************
# **** Dependencies ****
# **********************

FROM base AS dependencies

# Install poetry
RUN pip install --no-cache-dir \
      poetry==1.1.8

# Copy environment files
COPY poetry.lock pyproject.toml ./
      
# - Added `--no-root` per: https://github.com/python-poetry/poetry/issues/2549
RUN poetry install --no-root

# ******************
# **** Full App ****
# ******************

FROM dependencies AS full

# Bundle app source
COPY . .

# Spawn a shell within the virtual environment
# - Allows poetry environment to be discoverable when selecting python interpreter
CMD [ "poetry", "shell" ]

ENTRYPOINT [ "tail", "-f", "/dev/null" ]
# ********************
# **** Base Stage ****
# ********************
# **********************
# **** Dependencies ****
# **********************

FROM python:3.9.6-bullseye AS dependencies

WORKDIR /app

# Install poetry
RUN pip install --no-cache-dir \
      poetry==1.1.8

# Copy environment files
# - Note the checksum of this command will be different in remove environments (e.g. GitHub Actions)
#   Check if file permissions vary between local and remote
#
#   If the same remote environment pushes and pulls the images, the second time the cicd is run, the 
#   checksum should be the same
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

EXPOSE 5000

ENV FLASK_APP=src
ENV FLASK_ENV=development

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
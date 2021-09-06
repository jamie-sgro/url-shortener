# URL Shortener

[![Main Branch](https://github.com/jamie-sgro/url-shortener/actions/workflows/main.yml/badge.svg)](https://github.com/jamie-sgro/url-shortener/actions/workflows/main.yml) [![Dev Branch](https://github.com/jamie-sgro/url-shortener/actions/workflows/develop.yml/badge.svg)](https://github.com/jamie-sgro/url-shortener/actions/workflows/develop.yml)

This API handles the process of converting long URLs into shortcodes to ease the use of passing URLs between users and systems.



## Installation

- Ensure you have the latest version of Docker Desktop installed
- Run `sh environment/build.bash` from the root of the repository
  - In Windows, use Git Bash terminal, PowerShell, or equivalent to execute bash scripts
- To spin up containers, run `sh environment/start.bash` from the root of the repository



## Local Development

This repo makes use of Docker Dev environments. As such, follow the instructions found [here](https://code.visualstudio.com/docs/remote/containers). At minimum:

- Install the latest version of VSCode
- Install the Microsoft extension "Remote Development"
- Navigate to the "Remote Explorer" panel
- Select "Attach to Container" under the Container titled: "url-shortener: python"

## Testing

All tests can be found in `./tests` with a directory structure mirroring the directory structure of the files being tested

1. To use a container to run tests, run from the root of the repository:
```bash
docker-compose -p url-shortener -f environment/docker-compose.yml up pytest
```

2. To test locally, the containerized vscode IDE comes equipped with a test explorer, allowing you to run the whole suite, or cherry pick particular methods or classes.
These tests can also be ran in debug mode. For more info, review the currently installed extensions in your containerized vscode IDE with the keyword "test"

3. From the dev container CLI, tests can also be run with:
  1. To run only unit tests (faster) run the following:
      `poetry run pytest -m "not integration_test"`
  2. To run only integration tests (slower) run the following:
      `poetry run pytest -m integration_test`
  3. To run the whole test suit, run:
      `poetry run pytest`
  3. For any issues that arise, the `py.test -h` returns pytest's documentation
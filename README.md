# URL Shortener

[![Main Branch](https://github.com/jamie-sgro/url-shortener/actions/workflows/main.yml/badge.svg)](https://github.com/jamie-sgro/url-shortener/actions/workflows/main.yml) [![Dev Branch](https://github.com/jamie-sgro/url-shortener/actions/workflows/develop.yml/badge.svg)](https://github.com/jamie-sgro/url-shortener/actions/workflows/develop.yml)

This API handles the process of converting long URLs into shortcodes to ease the use of passing URLs between users and systems.

## Using Url-Shortener

### Submit a Url
To submit a url to be shortened, submit a POST request to http://localhost:5000/api/v1/url, with the query parameter `url` included. A valid POST request could look like:
`http://localhost:5000/api/v1/url?url=google.ca`

### Submit a URL with a desired shortcode
To submit a url to be shortened with a desired shortcode in mind, submit a POST request to http://localhost:5000/api/v1/url, with the query parameter `url` *and* `desired-shortcode` included. A valid POST request could look like:
http://localhost:5000/api/v1/url?url=https://github.com/jamie-sgro/url-shortener&desired-shortcode=github

### Redirecting using a shortcode

To redirect to a url using a shortcode, submit a GET request to `http://localhost:5000/api/v1/shortcode/<shortcode>`. A valid GET reqeust could look like:
`http://localhost:5000/api/v1/shortcode/hdf4oc`

- If a desired shortcode was specified, like the `github` shortcode example above, the following would direct to this repository's main page:
`http://localhost:5000/api/v1/shortcode/github`

### Retrieving Stats & Metadata

To view stats about the shortcodes themselves, submit a GET request to `http://localhost:5000/api/v1/shortcode/<shortcode>/stats`

This query would return something similar to the following:

```
date registered: 2021-09-06 22:36:19
last accessed: 2021-09-06 22:36:27
access count: 1
```



## Installation

- Ensure you have the latest version of Docker Desktop installed
- Run `sh environment/build.bash` from the root of the repository
  - In Windows, use Git Bash terminal, PowerShell, or equivalent to execute bash scripts
- To spin up containers, run `sh environment/start.bash` from the root of the repository
- Navigate to http://localhost:5000/ to view the frontend



## Local Development

*Note all containers are publicly hosted on AWS' Elastic Container Registry found here:*

https://gallery.ecr.aws/j2m0y8o3/url-shortener

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

3. From the dev container CLI, tests can also be run with any of the following:
    1. To run only unit tests (faster) run the following:
        `poetry run pytest -m "not integration_test"`
    2. To run only integration tests (slower) run the following:
        `poetry run pytest -m integration_test`
    3. To run the whole test suit, run:
        `poetry run pytest`
    4. For any issues that arise, the `py.test -h` returns pytest's documentation

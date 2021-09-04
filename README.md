# URL Shortener

This API handles the process of converting long URLs into shortcodes to ease the use of passing URLs between users and systems.



## Installation

- Ensure you have the latest version of Docker Desktop installed
- Run `sh environment/build.sh` from the root of the repository
  - In Windows, use Git Bash terminal, PowerShell, or equivalent to execute bash scripts
- To spin up containers, run `sh environment/start.sh` from the root of the repository



## Local Development

This repo makes use of Docker Dev environments. As such, follow the instructions found [here](https://code.visualstudio.com/docs/remote/containers). At minimum:

- Install the latest version of VSCode
- Install the Microsoft extension "Remote Development"
- Navigate to the "Remote Explorer" panel
- Select "Attach to Container" under the Container titled: "url-shortener: python"


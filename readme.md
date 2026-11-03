# Sample Credential Provider (Python)

A minimal Flask TPA sample showing the shape of a credential-provider app. It does **not** connect to a real vault: the `vault` action recognizes one demonstration query and returns placeholder credentials; all other queries return an error.

## API

- `GET /manifest` advertises the `vault` action.
- `POST /execute` handles that action and returns the sample credential result.

## Run locally

Requires Python 3 and pip.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

The direct Python entry point listens on `0.0.0.0:3000`.

A Docker image can be built with `docker build -t credential-provider .`. The included Dockerfile starts Flask’s CLI, whose default port is **5000**:

```sh
docker run --rm -p 5000:5000 credential-provider
```

## Security and limitations

This sample has no authentication or production vault integration and prints the requested lookup value to its logs. It is intentionally unsuitable for internet exposure. Replace the demonstration lookup with a secured secret manager integration before use; never return or log real credentials unnecessarily.

<!-- bigidsecure-community-guidance -->
## BigID Community

This repository is part of [BigID Community](https://github.com/bigidsecure), a place for community members to share code, integrations, examples, and projects with other BigID customers.

Project ownership and support vary by repository. Check the maintainers, license, prerequisites, and compatibility notes before use, and validate the project in your own environment. Unless this repository explicitly says otherwise, do not assume the project is officially supported or maintained by BigID.

Please do not commit credentials, customer data, or other confidential information. Check this repository’s contribution guidance before submitting changes.

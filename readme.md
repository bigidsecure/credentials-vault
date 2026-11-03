# Sample Credential Provider App

This application shows a sample implementation of a BigID app that supplies credentials from a credential vault.

**This sample application does not implement any security and should not be exposed to the wider internet**

## Setup

Install dependencies with pip install:

`pip3 install -r requirements.txt`

run the application by running:

`python3 app.py`

The application will then be accessible on port 3000.

## Customization

By default this application will provide the username password combination user:pass when passed the query "test" from BigID. 

Edit line 32 of app.py to change that behavior.

## Deployment

A dockerfile is included to build this application inside your own infra.

<!-- bigidsecure-community-guidance -->
## BigID Community

This repository is part of [BigID Community](https://github.com/bigidsecure), a place for community members to share code, integrations, examples, and projects with other BigID customers.

Project ownership and support vary by repository. Check the maintainers, license, prerequisites, and compatibility notes before use, and validate the project in your own environment. Unless this repository explicitly says otherwise, do not assume the project is officially supported or maintained by BigID.

Please do not commit credentials, customer data, or other confidential information. Check this repository’s contribution guidance before submitting changes.

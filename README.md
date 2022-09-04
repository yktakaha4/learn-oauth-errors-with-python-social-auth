# learn-oauth-errors-with-python-social-auth

## Prerequirements

- Python 3.10
  - Poetry
- [Direnv](https://github.com/direnv/direnv) (optional)

## Usage

### Register a new OAuth Application

https://github.com/settings/applications/new

| Name | Value |
| -- | -- |
| Application name | Your application name |
| Homepage URL | Your repository URL |
| Authorization callback URL | http://localhost:8000/social/complete/github |

Then, click `Generate a new client secret`, copy `Client ID` and `Client secrets`

### Run Server

```
# set secrets
$ cp -p .envrc.sample .envrc
$ direnv allow

$ poetry install

$ poetry run ./manage.py migrate

$ poetry run ./manage.py runserver
```

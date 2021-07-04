# Python Microservice Template
Python microservice template, inspired by my Kotlin based microservice template https://github.com/debuglevel/greeting-microservice, but with way less enthusiasm; and I'm not too sure that too much works here, because I just copied a bunch of stuff from my various other projects to have them at one place at least. 

## Development environment
* PyCharm Community
* venv
* Python 3.8

## venv stuff
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 rest.py --help
```

## TODO
* docker-compose
* dev cheat sheet
* Logging that does not completely suck
  * would nice to be configurable via ENV
* Testing?
  * tox (which seems to test against different Python versions. WTF compatibility? But it does not install those environments/python versions!)
* linting?
* Formatting?

##
pandoc Docker
Works in PowerShell with WSL1: docker build -t youtrack-release-notes . ; docker run -ti -v "${PWD}/out:/data" youtrack-release-notes (docker build -t youtrack-release-notes .) -and (docker run -ti -v "${PWD}/out:/data" youtrack-release-notes)

Youtrack-release-notes docker
docker build -t youtrack-release-notes . ; docker run -ti --add-host youtrack.hosts:10.101.33.8 --env-file=environment.prod -v "${PWD}/out.docker:/app/out" youtrack-release-notes

## Python cheat sheet

### Environment

#### Initialize virtual environment (using venv)

```sh
python3 -m venv venv
```

#### Activate virtual environment

```sh
source ./venv/bin/activate
```

### Dependencies

#### Install dependencies

```sh
pip install -r requirements.txt -r requirements-dev.txt
```

### Deployment

#### Development

```sh
uvicorn app.rest:fastapi --port=8080 --reload --log-config=app/logging-config.yaml
```

#### Production
This should be quite okay:
```sh
uvicorn app.rest:fastapi --port=8080 --log-config=app/logging-config.yaml
```

But some docs mention that `gunicorn` can be used as a manager.

### Documentation

#### Display OpenAPI documentations

Open http://localhost:8000/docs or http://localhost:8000/redoc

### Development

#### Dependency updates

`pip list --outdated` shows outdated (transitive) dependencies.

#### Formatting
##### black
`black` is used for formatting, because `black` does not ask about your opinion about how Python code should be formatted.
```bash
pip3 install black
black .
```

### Testing

#### Run tests

```sh
pytest
```

#### Run tests on every file change

```sh
pytest-watch
pytest-watch -c # clear terminal before pytest runs
```

#### Run test against different Python environments
```sh
tox
```
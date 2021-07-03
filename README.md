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
python3 main.py --help
```

## TODO
* docker-compose
* dev cheat sheet
* basic Flask stuff
  * use FastAPI instead of Flask.
* maybe even OpenAPI
* Logging that does not completely suck
* is using FastAPI like in https://github.com/debuglevel/labelprinter-microservice/tree/master/app a god idea?
* Testing?
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

#### Start development mode

```sh
uvicorn app.main:fastapi --port 8080 --reload --log-config logging-config.yaml
```

#### Start production mode
No idea, maybe use the command from the Dockerfile or look it up at https://fastapi.tiangolo.com/

### Documentation

#### Display OpenAPI documentations

Open http://localhost:8000/docs or http://localhost:8000/redoc

### Development

#### Dependency updates

`pip list --outdated` shows outdated (transitive) dependencies.

#### Formatting
# TODO: maybe use black instead?
`yapf` is used to format Python files. Use `yapf -p -r -i -e venv .` on project root to format all files.

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
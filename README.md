# route-logger-be

Backend for the Route Logger application.

Front end projext found [here](https://github.com/PearlisSad/route-logger-fe).

## Setup

- Install pyenv.
- Install python according to version specified in `.python-version`.
- Install packages with `pip install -r ./requirements.txt`.
- Create python virtual env `python -m venv`.

## Running

- Activate venv if not already active
  - Mac/Linux: `source <venv directory>/bin/activate`.
  - Windows: `workon MyProjectEnvt`
- Apply migrations `python manage.py migrate`.
- Run server `python manage.py runserver`.
- `workon MyProjectEnvt`

# Route Logger Backend

## Setup

## Running

- Activate venv if not already active
  - Mac/Linux: `source <venv directory>/bin/activate`.
  - Windows: `workon MyProjectEnvt`
- Apply migrations `python manage.py migrate`.
- Run server `python manage.py runserver`.
- `workon MyProjectEnvt`

## Description

Backend for the Route Logger application.
Django project that uses REST api to communicate with React frontend.
Front end projext found [here](https://github.com/PearlisSad/route-logger-fe).

- **Django** – Python backend framework used to handle server-side logic and database models.
- **django-cors-headers** – Enables Cross-Origin Resource Sharing (CORS) to allow requests from the React frontend.
- **djangorestframework** – Provides tools for building RESTful APIs, including serialization, authentication, and class-based views.

## Getting Started

### Setup

- Install pyenv.
- Install python according to version specified in `.python-version`.
- Install packages with `pip install -r ./requirements.txt`.
- Create python virtual env `python -m venv`.
  - See docs for more information -[Create Python Virtual Environment](https://docs.python.org/3/library/venv.html)
- Start Virtual Environment
  - Windows: `venv\Scripts\Activate.ps1`
  - Mac: `source venv/bin/activate`
- To deactivate the Virtual Environment, just execute `deactivate` while the Virtual Environment is running.

### Running

- Activate venv if not already active
  - Mac/Linux: `source <venv directory>/bin/activate`.
  - Windows: `workon MyProjectEnvt`
- Apply migrations `python manage.py migrate`.
- Run server `python manage.py runserver`.
- `workon MyProjectEnvt`

### Dependencies

- Python 3.10+

## Authors

[Rapha](https://github.com/PearlisSad)

[Jun](https://github.com/JunSmith)

## Acknowledgments

Inspiration, code snippets, etc.

- [Django React Authentication](<[https://github.com/matiassingers/awesome-readme](https://github.com/desphixs/JWT-Django-Rest-Framework-React)>)

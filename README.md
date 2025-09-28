# Route Logger Backend

FastAPI REST API for [Route Logger FE project](https://github.com/PearlisSad/route-logger-fe).

## Initial setup

- [Install pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#a-getting-pyenv).
- Install python according to version specified in `.python-version`: `pyenv local "$(cat .python-version)"`.
- Create python virtual env `python -m venv .venv`. You should notice in your command line a `(.venv)` at the start of it.
  - See docs for more information -[Create Python Virtual Environment](https://docs.python.org/3/library/venv.html)
- Install packages with `pip install -r ./requirements.txt`.
  - Note that when adding dependencies to the project, add them to `src/requirements/requirements.in`.
  - The changes should then be reflected to the requirements.txt by running `pip-compile --strip-extras src/requirements/requirements.in`
- Start Virtual Environment
  - Windows: `venv\Scripts\Activate.ps1`
  - Mac: `source venv/bin/activate`
- To deactivate the Virtual Environment, just execute `deactivate` while the Virtual Environment is running.

## Running

- Activate venv if not already active
  - Mac/Linux: `source <venv directory>/bin/activate`.
  - Windows: `workon MyProjectEnvt`
- Install the dependencies if not already present: `pip install -r requirements.txt`
- Export the desired MongoDB URL address. For local it should be: `export MONGODB_URL="mongodb://localhost:27017"`
- Run the service using: `uvicorn src.main:app --reload`

Now you can load http://localhost:8000/docs in your browser.

### Dependencies

- Python 3.10+

## Authors

- [Rapha](https://github.com/PearlisSad)
- [Jun](https://github.com/JunSmith)

## Acknowledgments

Inspiration, code snippets, etc.

- [Django React Authentication](https://github.com/desphixs/JWT-Django-Rest-Framework-React)
- [FastAPI Quick Start blog post](https://developer.mongodb.com/quickstart/python-quickstart-fastapi/)

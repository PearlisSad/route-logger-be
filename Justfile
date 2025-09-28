requirements: 
  echo 'Executing requirements'
  pip-compile --strip-extras requirements.in
  pip-compile --strip-extras dev-requirements.in

run: 
  echo 'Executing run'
  uvicorn src.main:app --reload

test: 
  pytest


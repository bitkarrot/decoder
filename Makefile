all: format check

format: prettier isort black

check: pyright pylint flake8 checkisort checkblack checkprettier

prettier:
	poetry run ./node_modules/.bin/prettier --write config.json manifest.json static templates

pyright:
	poetry run ./node_modules/.bin/pyright

black:
	poetry run black .

flake8:
	poetry run flake8

mypy:
	poetry run mypy

isort:
	poetry run isort .

pylint:
	poetry run pylint *.py

checkprettier:
	poetry run ./node_modules/.bin/prettier --check config.json manifest.json static templates

checkblack:
	poetry run black --check .

checkisort:
	poetry run isort --check-only .

test:
	PYTHONUNBUFFERED=1 \
	DEBUG=true \
	poetry run pytest

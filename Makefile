.PHONY: run test lint format build

run:
	poetry run python -m sitegen.main

test:
	poetry run pytest tests/ -v
	poetry run behave features/

lint:
	poetry run ruff check sitegen/ features/ tests/

format:
	poetry run ruff format sitegen/ features/ tests/

build:
	podman build -t sitegen -f Containerfile .

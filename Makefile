.PHONY: run audit fix clean

all: help

dev:
	@uv run granian --interface asgi --reload --loop uvloop --workers 1 --log app.main:api

audit:
	@echo "Checking code for linting errors (ruff)..."
	uv tool run ruff check . --config pyproject.toml
	@echo "Checking code for formatting errors (ruff)..."
	uv tool run ruff format . --check --config pyproject.toml

fix:
	@echo "Fixing code for linting errors (ruff)..."
	uv tool run ruff check . --config pyproject.toml --fix
	@echo "Fixing code for formatting errors (ruff)..."
	uv tool run ruff format . --config pyproject.toml

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache

help:
	@echo "Usage: make <target>"
	@echo "  dev      Run the application in development mode"
	@echo "  audit    Check the code quality"
	@echo "  fix      Fix the code quality"
	@echo "  clean    Clean the project files"

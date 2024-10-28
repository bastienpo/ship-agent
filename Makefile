.PHONY: audit fix clean

all: help

audit:
	@echo "Checking code for linting errors (ruff)..."
	uv tool run ruff check libs --config pyproject.toml
	@echo "Checking code for formatting errors (ruff)..."
	uv tool run ruff format libs --check --config pyproject.toml

fix:
	@echo "Fixing code for linting errors (ruff)..."
	uv tool run ruff check libs --config pyproject.toml --select I --fix
	@echo "Fixing code for formatting errors (ruff)..."
	uv tool run ruff format libs --config pyproject.toml

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache

help:
	@echo "Usage: make <target>"
	@echo "  audit    Check the code quality"
	@echo "  fix      Fix the code quality"
	@echo "  clean    Clean the project files"

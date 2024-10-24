.PHONY: run clean

dev:
	@uv run granian --interface asgi --reload --loop uvloop --workers 1 --log app.main:api

audit:
	uv run ruff check . --config pyproject.toml
	uv run ruff format . --check --config pyproject.toml

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache

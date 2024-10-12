.PHONY: run dev clean quality

run:
	uv run granian --interface asgi --workers 4 --threads 4 --loop uvloop app.main:api

dev:
	@echo "Starting development server..."
	@uv run granian --interface asgi --reload --loop uvloop --workers 1 app.main:api

clean:
	@echo "Cleaning the project files..."
	rm -rf **/*.pyc **/__pycache__
	rm -rf .pytest_cache
	ruff clean

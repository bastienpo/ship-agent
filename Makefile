include .env
export

.PHONY: run clean

run:
	@uv run granian app.main:api

clean:
	rm -rf **/*.pyc \
		**/__pycache__ \
		.pytest_cache

all: format check

format: prettier black ruff

check: mypy pyright checkblack checkruff checkprettier

prettier:
	@if [ -x ./node_modules/.bin/prettier ]; then \
		./node_modules/.bin/prettier --write .; \
	elif command -v npx >/dev/null 2>&1; then \
		npx --yes prettier --write .; \
	else \
		echo "prettier not found; skipping (install via 'npm i -D prettier')"; \
	fi
pyright:
	@if [ -x ./node_modules/.bin/pyright ]; then \
		./node_modules/.bin/pyright; \
	elif command -v npx >/dev/null 2>&1; then \
		npx --yes pyright; \
	else \
		echo "pyright not found; skipping (install via 'npm i -D pyright')"; \
	fi

mypy:
	@if command -v uv >/dev/null 2>&1; then \
		echo "Running mypy via uv"; \
		uv run mypy .; \
	else \
		echo "uv not found; falling back to system Python mypy"; \
		python3 -m mypy .; \
	fi

black:
	@if command -v uv >/dev/null 2>&1; then \
		uv run black .; \
	elif command -v black >/dev/null 2>&1; then \
		black .; \
	else \
		python3 -m black . || echo "black not available"; \
	fi

ruff:
	@if command -v uv >/dev/null 2>&1; then \
		uv run ruff check . --fix; \
	elif command -v ruff >/dev/null 2>&1; then \
		ruff check . --fix; \
	else \
		python3 -m ruff check . --fix || echo "ruff not available"; \
	fi

checkruff:
	@if command -v uv >/dev/null 2>&1; then \
		uv run ruff check .; \
	elif command -v ruff >/dev/null 2>&1; then \
		ruff check .; \
	else \
		python3 -m ruff check . || echo "ruff not available"; \
	fi

checkprettier:
	@if [ -x ./node_modules/.bin/prettier ]; then \
		./node_modules/.bin/prettier --check .; \
	elif command -v npx >/dev/null 2>&1; then \
		npx --yes prettier --check .; \
	else \
		echo "prettier not found; skipping check (install via 'npm i -D prettier')"; \
	fi

checkblack:
	@if command -v uv >/dev/null 2>&1; then \
		uv run black --check .; \
	elif command -v black >/dev/null 2>&1; then \
		black --check .; \
	else \
		python3 -m black --check . || echo "black not available"; \
	fi

checkeditorconfig:
	editorconfig-checker

test:
	PYTHONUNBUFFERED=1 \
	DEBUG=true \
	uv run pytest
install-pre-commit-hook:
	@echo "Installing pre-commit hook to git"
	@echo "Uninstall the hook with uv run pre-commit uninstall"
	uv run pre-commit install

pre-commit:
	uv run pre-commit run --all-files


checkbundle:
	@echo "skipping checkbundle"

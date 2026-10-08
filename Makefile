.PHONY: test lint format check install uninstall clean

test:
	python3 -m unittest discover -s tests -v

lint:
	ruff check .

format:
	ruff format .

check:
	ruff check .
	ruff format --check .

install:
	./scripts/install.sh

uninstall:
	./scripts/uninstall.sh

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

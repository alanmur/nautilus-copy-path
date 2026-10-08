.PHONY: test install uninstall clean

test:
	python3 -m unittest discover -s tests -v

install:
	./scripts/install.sh

uninstall:
	./scripts/uninstall.sh

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

PROJECT_NAME = myfastapi
TEST_FOLDER = tests
APPLICATION = myfastapi.api.main:app

.PHONY: default
default: help

.PHONY: help
help:
	@echo "All Commands:"
	@echo "	Env:"
	@echo "		clean - Remove temp files."
	@echo "		run - Run application in development mode."

.PHONY: clean
clean:
	- @find . -name "*.pyc" -exec rm -rf {} \;
	- @find . -name "__pycache__" -delete
	- @find . -name "*.pytest_cache" -exec rm -rf {} \;
	- @find . -name "*.mypy_cache" -exec rm -rf {} \;

.PHONY: run
run:
	uvicorn $(APPLICATION) --reload


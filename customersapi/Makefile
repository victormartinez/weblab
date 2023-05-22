PROJECT_NAME = myflaskapi
TEST_FOLDER = tests
APPLICATION = customers.main:app

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
	FLASK_DEBUG=1 FLASK_APP=${FLASK_APP} flask run

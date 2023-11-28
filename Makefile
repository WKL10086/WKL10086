# HELP
# This will output the help for each task
# src: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help test

.DEFAULT_GOAL := help

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

test: ## Run tests
	tsc src/test.ts && node src/test.js
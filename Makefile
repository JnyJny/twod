
# twod makefile

EPHEMERAL= .coverage .pytest_cache htmlcov dist twod.egg-info

OLD= "0.1.2"
NEW= "0.1.3"

VERSIONED_FILES= pyproject.toml tests/test_twod.py twod/__init__.py

POETRY= poetry

.PHONY: build publish test cov $(VERSIONED_FILES)

all:

	@echo Help:
	@echo "   make version $(OLD) to $(NEW)"
	@echo "   make build"
	@echo "   make publish"
	@echo "   make test"
	@echo "   make cov"
	@echo "   make clean"

version:
	sed -i '' -e 's/$(OLD)/$(NEW)/' pyproject.toml
	sed -i '' -e 's/$(OLD)/$(NEW)/' twod/__init__.py
	sed -i '' -e 's/$(OLD)/$(NEW)/' tests/test_twod.py
	git commit -m 'updated VERSION to $(NEW)' $(VERSIONED_FILES)
	git tag $(NEW)
	git push --tags

format:
	black -l 79 -q .

build:
	$(POETRY) build

publish: build
	$(POETRY) publish

test:
	pytest --cov=.

cov:
	pytest --cov=. --cov-report=html

clean:
	-@find . -name \*,cover -exec rm '{}' \;
	-@find . -name \*~ -exec rm '{}' \;
	-@/bin/rm -rf $(EPHEMERAL)

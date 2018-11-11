# twod makefile

ROOT=.

EPHEMERAL= .coverage .pytest_cache htmlcov dist twod.egg-info

OLD= "0.1.3"
NEW= "0.1.4"

VERSIONED_FILES= pyproject.toml tests/test_twod.py twod/__init__.py

POETRY= poetry

BLACK_OPTS= -l 79 -q

.PHONY: build publish test cov $(VERSIONED_FILES)

all:

	@echo Help:
	@echo "   make version $(OLD) to $(NEW)"
	@echo "   make format, runs black $(BLACK_OPTS)"
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
	black $(BLACK_OPTS) $(ROOT)

build:
	$(POETRY) build

publish: build
	$(POETRY) publish

test:
	pytest --cov=$(ROOT)

cov:
	pytest --cov=$(ROOT) --cov-report=html

clean:
	-@find . -name \*,cover -exec rm '{}' \;
	-@find . -name \*~ -exec rm '{}' \;
	-@/bin/rm -rf $(EPHEMERAL)

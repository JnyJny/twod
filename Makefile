
# twod makefile

EPHEMERAL= .coverage .pytest_cache htmlcov dist twod.egg-info


OLDVERSION= "0.1.1"
VERSION= "0.1.2"

VERSIONED_FILES= pyproject.toml tests/test_twod.py twod/__init__.py

POETRY= poetry

.PHONY: build publish test cov $(VERSIONED_FILES)

version:
	sed -i '' -e 's/$(OLDVERSION)/$(VERSION)/' pyproject.toml
	sed -i '' -e 's/$(OLDVERSION)/$(VERSION)/' twod/__init__.py
	sed -i '' -e 's/$(OLDVERSION)/$(VERSION)/' tests/test_twod.py

build:
	$(POETRY) build

publish: build
	$(POETRY) publish

test:
	pytest --cov=.

cov:
	pytest --cov=. --cov-report=html

clean:
	@/bin/rm -rf $(EPHEMERAL)

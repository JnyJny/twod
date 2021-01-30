# twod makefile

PACKAGE= twod
ROOT=.

EPHEMERAL= .coverage .pytest_cache htmlcov dist twod.egg-info

.PHONY: major_release minor_release patch_release \
   MAJOR MINOR PATCH update push publish test cov report

all:
	@echo Help:
	@echo "   make major_release"
	@echo "   make minor_release"
	@echo "   make patch_release"
	@echo "   make build"
	@echo "   make publish"
	@echo "   make test"
	@echo "   make cov"
	@echo "   make report - dumps HTML coverage report"
	@echo "   make clean"


major_release: test MAJOR update push publish

minor_release: test MINOR update push publish

patch_release: test PATCH update push publish


MAJOR:
	@poetry version major

MINOR:
	@poetry version minor

PATCH:
	@poetry version patch

update:
	@git add pyproject.toml
	@git commit -m `poetry version -s`
	@git tag `poetry version -s`

push: 
	@git push --tags origin master

publish: 
	@poetry build
	@poetry publish

test:
	@pytest

cov:
	pytest --cov=$(ROOT)/$(PACKAGE)

report:
	pytest --cov=$(ROOT)/$(PACKAGE) --cov-report=html

clean:
	-@find . -name \*,cover -exec rm '{}' \;
	-@find . -name \*~ -exec rm '{}' \;
	-@/bin/rm -rf $(EPHEMERAL)


# twod makefile

EPHEMERAL= .coverage .pytest_cache htmlcov

test:
	pytest --cov=.

cov:
	pytest --cov=. --cov-report=html

clean:
	@/bin/rm -rf $(EPHEMERAL)

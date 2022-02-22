install:
	poetry install

brain-games:
	poetry run brain-games

Build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

.PHONY: install test lint selfcheck check build

lint:
	autopep8 --in-place --recursive --exclude venv .

tests:
	pytest -rf -v

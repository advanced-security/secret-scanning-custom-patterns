all: requirements lint
.PHONY: lint requirements

requirements:
	python3 -m pip install -r requirements.txt > /dev/null 

lint:
	python3 -m pip install -r dev-requirements.txt > /dev/null
	python3 -m yapf -i --style='{based_on_style: google, column_limit: 120, indent_width: 4}' test.py
	ruff --ignore=E501 test.py
	python3 -m flake8 --ignore=E501,W504,E124 test.py
	yes | python3 -m mypy --install-types
	python3 -m mypy --no-error-summary --ignore-missing-imports --strict test.py
	python3 -m bandit --quiet -r . # --configfile bandit.yml


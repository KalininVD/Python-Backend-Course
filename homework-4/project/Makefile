PIP = venv\scripts\pip.exe
PYTHON = venv\scripts\python.exe
PYTEST = venv\scripts\pytest.exe

venv:
	python -m venv venv

install_requirements:
	${PYTHON} -m pip install --upgrade pip
	${PIP} install -r requirements.txt

run:
	${PYTHON} server.py

tests:
	${PYTEST} -v ./test_controllers.py
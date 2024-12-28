PIP = venv\scripts\pip.exe
PYTHON = venv\scripts\python.exe
PYTEST = venv\scripts\pytest.exe

clear:
	rmdir /s /q venv

venv:
	python -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

run:
	${PYTHON} server.py

tests:
	${PYTEST}  -v ./test_controllers.py
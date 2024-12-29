# Python-Backend-Course
Repository with all materials for the Python-Backend Course (HSE SE 2 year)

# Homework 4
Currently implemented:
- Flask app ([server.py](./homework-4/project/server.py))
- Sum operation ([controllers.py](./homework-4/project/controllers.py))
- Tests for the sum operation ([test_controllers.py](./homework-4/project/test_controllers.py))
- Makefile for running the app and tests ([Makefile](./homework-4/project/Makefile))

### Tests

For testing the app, Windows 11 was used with Python 3.12.3 virtual environment.

Python libraries versions:
- flask: 3.1.0
- python-dotenv: 1.0.1
- pytest: 8.3.4

According to PyTest, all 7 tests passed successfully, so the sum operation is implemented correctly.

**NOTE**: The app was tested on Windows 11, so the `clear` option was removed from the `Makefile` due to the problems with deleting non-empty directories inside the makefile. Original `Makefile` is the `Makefile.old` file, probably it will work on MacOS and Linux, but that was not tested.
# Flask app

Simple Flask app by VDK.

## Usage

To start the app, first create a virtual environment and install the requirements:

```bash
make venv
make install_requirements
```

Then run the app:

```bash
make run
```

## Tests

To run the tests, virtual environment must be created and all the requirements must be installed.

Then run the tests with:

```bash
make tests
```

## Notes

- The app is running on port `5000` by default.
- The app is running in debug mode by default.
- For changing the port or the debug mode, edit the `.env` file.
- The only supported operation is currently in `controllers.py` file, it sums two numbers.
- The app was tested on Windows 11, so the `clear` option was removed from the `Makefile` due to the problems with deleting non-empty directories from the shell. Original `Makefile` is the `Makefile.old` file, probably it will work on MacOS and Linux, but that was not tested.
- The app was tested with Python 3.12.3, pytest tests ran successfully (7 out of 7 tests passed).
# coursecode

This repository contains the Python helper package used in this course.

## What this package is for

You will use this package in some assignments and notebooks.

Once installed, you can import it in Python like this:

```python
import coursecode
```

or, for specific tools:

```python
from coursecode import some_function
```

## Installation

Please install the package in the same Python environment that you use for VS Code or Jupyter.

Open a terminal and run:

```bash
python -m pip install "coursecode @ git+https://github.com/umutozge/coursecode.git"
python -m pip install "coursecode @ git+https://github.com/umutozge/coursecode.git"
```

If `python` does not work on your system, try:

```bash
python3 -m pip install "coursecode @ git+https://github.com/umutozge/coursecode.git"
python3 -m pip install "coursecode @ git+https://github.com/umutozge/coursecode.git"
```

## Upgrading to the newest version

From time to time, the package may be updated during the semester.

To upgrade to the newest version, run:

```bash
python -m pip install --upgrade "coursecode @ git+https://github.com/umutozge/coursecode.git"
python -m pip install --upgrade "coursecode @ git+https://github.com/umutozge/coursecode.git"
```

## Checking that installation worked

After installation, test it with:

```bash
python -c "import coursecode; print('coursecode installed successfully')"
```

If you are using Jupyter, you can also test in a notebook cell:

```python
import coursecode
```

If that runs without an error, the installation worked.

## VS Code

If you use VS Code, make sure the selected Python interpreter is the same one where you installed the package.

You can check the interpreter in VS Code from the Command Palette with:

- `Python: Select Interpreter`

If the import still fails in VS Code, open the built-in terminal and run:

```bash
python -c "import sys; print(sys.executable)"
```

Then compare that path with the interpreter shown by VS Code.

## JupyterLab

The package must be installed in the same Python environment as the notebook kernel.

If `import coursecode` fails in Jupyter even though installation succeeded in the terminal, your notebook may be using a different Python environment.

In a notebook cell, run:

```python
import sys
print(sys.executable)
```

In a terminal, run:

```bash
python -c "import sys; print(sys.executable)"
```

These should usually point to the same environment.

## Common problems

### `ModuleNotFoundError: No module named 'coursecode'`

Usually this means one of these:

- The package was not installed successfully.
- You installed it in a different Python environment.
- Jupyter is using a different kernel than the one where you installed the package.

Try reinstalling with:

```bash
python -m pip install --upgrade "coursecode @ git+https://github.com/umutozge/coursecode.git"
python -m pip install --upgrade "coursecode @ git+https://github.com/umutozge/coursecode.git"
```

### `pip` command not found

Try using:

```bash
python -m pip install "coursecode @ git+https://github.com/umutozge/coursecode.git"
python -m pip install "coursecode @ git+https://github.com/umutozge/coursecode.git"
```

instead of just `pip install ...`.

### Git is not installed

Installing directly from GitHub may require Git to be installed on your system.

If the install fails with a message related to `git`, install Git first and then rerun the command.

## Recommended habit

Before starting a new assignment, it is a good idea to run:

```bash
python -m pip install --upgrade "coursecode @ git+https://github.com/umutozge/coursecode.git"
python -m pip install --upgrade "coursecode @ git+https://github.com/umutozge/coursecode.git"
```

This helps ensure that you have the latest course version.

## Getting help

If installation fails, include the full error message when asking for help.
Copying the exact terminal output is more useful than sending a screenshot.

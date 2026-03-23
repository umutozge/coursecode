# coursepy

This repository contains the Python helper package used in this course.

## What this package is for

You will use this package in some assignments and notebooks.

Once installed, you can import it in Python like this:

```python
import coursepy
```

or, for specific tools:

```python
from coursepy import some_function
```

## Installation

Please install the package in the same Python environment that you use for VS Code or Jupyter.

Open a terminal and run:

```bash
python -m pip install "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

If `python` does not work on your system, try:

```bash
python3 -m pip install "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

## Upgrading to the newest version

From time to time, the package may be updated during the semester.

To upgrade to the newest version, run:

```bash
python -m pip install --upgrade "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

## Checking that installation worked

After installation, test it with:

```bash
python -c "import coursepy; print('coursepy installed successfully')"
```

If you are using Jupyter, you can also test in a notebook cell:

```python
import coursepy
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

If `import coursepy` fails in Jupyter even though installation succeeded in the terminal, your notebook may be using a different Python environment.

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

### `ModuleNotFoundError: No module named 'coursepy'`

Usually this means one of these:

- The package was not installed successfully.
- You installed it in a different Python environment.
- Jupyter is using a different kernel than the one where you installed the package.

Try reinstalling with:

```bash
python -m pip install --upgrade "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

### `pip` command not found

Try using:

```bash
python -m pip install "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

instead of just `pip install ...`.

### Git is not installed

Installing directly from GitHub may require Git to be installed on your system.

If the install fails with a message related to `git`, install Git first and then rerun the command.

## Recommended habit

Before starting a new assignment, it is a good idea to run:

```bash
python -m pip install --upgrade "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

This helps ensure that you have the latest course version.

## Getting help

If installation fails, include the full error message when asking for help.
Copying the exact terminal output is more useful than sending a screenshot.

## Using Conda (optional)

If you use Conda (Anaconda or Miniconda), you can install the package into a Conda environment.

1. Create a new environment for this course (recommended):

```bash
conda create -n course-env python=3.11
conda activate course-env
```

2. Install the course package *inside that environment*:

```bash
python -m pip install "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

3. To upgrade later, first `conda activate course-env`, then run:

```bash
python -m pip install --upgrade "coursepy @ git+https://github.com/umutozge/coursepy.git"
```

Make sure you always activate the same Conda environment before running Python, Jupyter, or VS Code for this course, so they all see the same installed packages.

### Using the Conda environment in Jupyter

If you use JupyterLab or Jupyter Notebook, make sure your notebook uses the same Conda environment where you installed the course package.

1. Activate your Conda environment and install `ipykernel` (once):

```bash
conda activate course-env
python -m pip install ipykernel
python -m ipykernel install --user --name course-env --display-name "Python (course-env)"
```

2. Start Jupyter from the same environment:

```bash
conda activate course-env
jupyter lab
```

3. In Jupyter, select the kernel:

- In the "Kernel" or "Select Kernel" menu, choose:  `Python (course-env)`

If a notebook still cannot import the package, check which Python it is using by running:

```python
import sys
print(sys.executable)
```

It should point to the `course-env` environment where you installed the package.

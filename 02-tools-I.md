# Tools I: Packaging and virtual-environments


## Python packages

- There are tens of thousands of python packages
- No need to write everything from scratch as there's probably already a package suitable for you out there
- Contributing to existing packages makes it more likely your work will be reused
- Contributing to open-source packages is the best way to learn how to code

## Python virtual environments

- Virtual environments isolate your setup from the rest of the system
- It ensures different project do not interfere with each other
- For instance, you could have:
  - a production environment with a tried and tested version of your software and tensorflow 1.15
  - a development environment with latest versions and a migration to tensorflow 2.1

## Package managers

Package managers help you install packages. Some help you install virtual environments too. 
Better known python package managers include
[conda](https://docs.conda.io/en/latest/), [pip](https://pip.pypa.io/en/stable/) and
[poetry](https://python-poetry.org/)

|                           | conda    | pip | poetry     |
|---------------------------|----------|-----|------------|
|audience                   | research | all | developers |
|manage python packages     | ✅       |  ✅ | ✅         |
|manage non-python packages | ✅       | ❌  | ❌         |
|choose python version      | ✅       | ❌  | ❌         |
|manage virtual envs        | ✅       | ❌  | ✅         |
|easy interface             | ❌       | ✅  | ❌         |
|fast                       | ❌       | ✅  | ✅         |

## Rules for choosing a package manager

1. Choose one
1. Stick with it
1. Don't change to a different package manager

We generally advise [conda](https://docs.conda.io/en/latest/) because it is the de facto
standard in science, and because it can natively install libraries such as
[fftw](https://anaconda.org/conda-forge/fftw),
[vtk](https://anaconda.org/conda-forge/vtk), or even Python, R, and Julia
themselves.

It is also now the de facto package manager and Python distribution on our HPC systems.

There are still one or two packages that conda can't install and for these you can still use pip, but 
within a virtual environment.


## Example

## Installing and using an environment

1. If you haven't already, see the initial instructions
   on how to install conda, Visual Studio Code and Git.

1. Create a new folder to use for this course. Avoid giving it a name that
   includes spaces. 
   
   Start Visual Studio Code and select
   "Open folder..." from the welcome screen. Navigate to the folder you just
   created and press "Select Folder".

1. Press "New file" and copy the below text. Save the file as
   `environment.yml`, the location should default to your newly created
   folder.

   ```yaml
   name: course
   dependencies:
     - python=3.6
     - flake8
     - pylint
     - black
     - mypy
     - requests
     - pip
     - R2T2
   ```

1. Create a new virtual environment using conda:

   **Windows users will want to start the app `Anaconda Prompt` from the Start
   Menu.**

   **Linux and Mac users should use a terminal app of their choice. You may
   see a warning with instructions. Please follow the instructions.**

   ```{bash}
   conda env create -f [path to environment.yml]
   ```

   You can obtain `[path to environment.yml]` by right clicking the file tab
   near the top of Visual Studio Code and selecting "Copy Path" from the
   drop-down menu. Right click on the window for your command line interface
   to paste the path.

1. We can now activate the environment:

   ```{bash}
   conda activate course
   ```

1. And check python knows about the installed packages. Start a Python
   interpreter with the command `python` then:

   ```{python}
   import requests
   ```

   We expect this to run and not fail. You can see the location of the
   installed package with:

   ```{python}
   requests.__file__
   ```

   ```
   'C:\\ProgramData\\Anaconda3\\envs\\course\\lib\\site-packages\\requests\\__init__.py'
   ```
   

   The file path you see will vary but note that it is within a directory
   called `course` that contains the files for the virtual environment you
   have created. Exit the Python interpreter:

   ```{python}
   exit()
   ```

1. Finally, feel free to remove `requests` from `environment.yml`, then run

   ```{bash}
   conda env update -f [path to environment.yml]
   ```

    and see whether the package has been updated or removed.


## Selecting an environment in Visual Studio Code

If you haven't already, see the initial instructions on how
to install Visual Studio (VS) Code.

On Linux and Mac, one option is to first activate your preferred conda environment, and then start VS Code:

```{bash}
conda activate name_of_environment
code .
```

The simplest option for all platforms to set the interpreter is via the
Command Palette:

- For Windows/Linux: Ctrl + Shift + P, and start typing "Python: Select
  interpreter"
- For macOS: Cmd + Shift + P, and start typing "Python: Select interpreter"

If you already have a Python file open then it's also possible to set the
interpreter using the toolbar at the bottom of the window.




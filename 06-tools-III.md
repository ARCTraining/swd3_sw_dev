# Tools 3: Linters and Linting

## What is linting?

Linters enforce [style rules](https://lintlyci.github.io/Flake8Rules/) on your
code such as:

- disallow one letter variables outside of loops
- use `lower_snake_case` for variables
- use `CamelCase` for classes
- disallow nesting more than n deep
- detect code-smells (patterns that are often bugs, e.g. two functions with the
  same name)
- static type detection ([mypy](http://mypy-lang.org/)) where we tell the editor
  what kind of objects (`dict`, `list`, `int`, etc) a function expects

Consistent styles make a code more consistent an easier to read, whether or not
you agree with the style. Using an automated linter avoids bike-shedding since
the linter is the final arbiter.

## Why does linting matter?

- Code is read more often than written
- Setting up a linter in your editor takes 5 minutes
- Those 5 minutes are redeemed across the lifetime of the project
- Linters shortcut the `edit-run-debug and repeat` workflow

## Rules for choosing linters

1. Choose a few
1. Stick with them

We chose:

- [flake8](https://pypi.org/project/black/) because it is simple
- [pylint](https://www.pylint.org/) because it is (too?) extensive
- [mypy](http://mypy-lang.org/) because it helps keep track of object types

## Exercise

Setup VS Code:

1. Open Settings (see [previous
    exercise](../l1-03-tools-II#rules-to-choose-a-code-formatter) if you're
    not sure how):
  - Search for "linting enable" and check the box for "Python Linting:
  Enabled".
  - Search for "pylint enabled" and check the box for "Python Linting:
  Pylint Enabled" (you may need to scroll down for this one).
  - Search for "pylint use" and **un**check the box for "Python Linting:
  Pylint Use Minimal Checkers".
  - Search for "flake8 enabled" and check the box for "Python Linting: Flake8
  Enabled".
  - Search for "mypy enable" and check the box for "Python Linting: Mypy
  Enabled".
1. Create a file `unlinted.py` with the following code and save it:

   ```python
   from typing import List


   class printer:
       pass


   def ActionatePrinters(printers: List[printer]):
       # pylint: disable=missing-docstring
       printing_actions = []
       for p in printers:

           if p == None:
               continue

           def action():
               print(p)

           printing_actions.append(action)

           p = "something"
           print(p)

       for action in printing_actions:
           action()


   ActionatePrinters([1, 2, 2])
   ```

1. Check the current errors (click on errors in status bar at the bottom)
1. Try and correct them
1. Alternatively, try and disable them (but remember: _with great power..._).
   We've already disabled-one at the function scope level. Check what happens
   if you move it to the top of the file at the module level.

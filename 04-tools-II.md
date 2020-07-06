# Tools (part 2)

## Why does formatting matter?

* Code is read more often than it is written
* Setting up a formatter in your editor takes 5 minutes
* Those 5 minutes are redeemed across the lifetime of the project

## Rules to choose a code formatter

1. Choose one
1. Stick with it

We suggest [black](https://pypi.org/project/black/) because it has very few
options with which to confuse you.

## Formatting example

Using Visual Studio Code:

1. Put the following into a file `myscript.py` and save it. If you are
prompted to install the Python extension then be sure to do so.

   ```python
   x = {  'a':37,'b':42,
   'c':927}
   y = 'hello '+       'world'
   class foo  (     object  ):
      def f    (self   ):
          return       y **2
      def g(self, x :int,
          y : int=42
          ) -> int:
          return x--y
   def f  (   a ) :
      return      37+-a[42-a :  y*3]
   ```

1. Ensure that you have activated your "course" conda environment using the
selector in the bottom panel of VS Code
1. Open Settings
  - macOS via `⌘ + ,` or menus: **Code Preferences Settings**
  - Windows/Linux via `Ctrl + ,` or menus: **File Preferences Settings**
1. Search for "python formatting provider" and choose "black"
1. Search for "format on save" and check the box to enable
1. Save the file again: it should be reformatted automagically
1. Now paste the code again but before saving delete a ':' somewhere. When
   saving, the code will likely not format. It is syntactically invalid.
   The formatter cannot make sense of the code and thus can't format it.

## Solution

 After saving, the code should be automatically formatted to:

 ```python
 x = {"a": 37, "b": 42, "c": 927}
 y = "hello " + "world"

 class foo(object):
     def f(self):
         return y ** 2

     def g(self, x: int, y: int = 42) -> int:
         return x - -y
 ```

See? Much improved formatting.

Still, the sharp-eyed user might notice at least one issue with this code.
*Formatting code does not make it less buggy!*

# Data Types and Data Structures

# What is a data structure?

```yaml
data structure: represents information and how that information can be accessed
```

Choosing the right representation for your data can vastly simplify your code
and increase performance.

Choosing the wrong representation can melt your brain. Slowly.

## Examples:

The number `2` is represented with the integer `2`

```python
type(2)
int
```

Acceptable behaviors for integers include `+`, `-`, `*`, `/`

```python
1 + 2
3
1 - 2
-1
```

On the other hand, text is represented by a string

```python
type("text")
str
```

It does *not* accept all the same behaviours as an integer:

```python
"a" + "b"
"ab"
"a" * "b"
TypeError: can't multiply sequence by non-int of type 'str'
```

Integers *can* be represented as strings, but their behaviours would be
unexpected:

```python
"1" + "2"
"12"
```

With integers, `+` is an *addition*, for strings it's a *concatenation*.

## Impact of choosing the wrong data structure

- we could use `"1", "2", "3"` (ie. strings) to represent integers, rather than `1`, `2`, `3`
- we would have to reinvent how to add numbers, and multiply, and divide them
- the wrong data structures can make your code vastly more complicated
- also, the code would be quite slow

Stay sensible. Stop and choose the right data structure for you!


# Basic data structures

## Lists

Lists are containers of other data:

```python
# List of integers
[1, 2, 3]
# List of strings
["a", "b", "b"]
# List of lists of integers
[[1, 2], [2, 3]]
```

Lists make sense when:

- you have more than one item of data
- the items are somehow related: Lists of apples and oranges are a code-smell

   ```python
   [1, 2, 3]  # might be the right representation
   ["a", 2, "b"]  # probably wrong
   ```

- the items are ordered and can be accessed

   ```python
   velocities_x = [0.3, 0.5, 0.1]
   velocities_x[1]  # e.g. could be velocity a point x=1
   ```

Beware! The following might indicate a list is the wrong data structure:

   - apples and oranges
   - deeply nested list of lists of lists

## Other languages
* C++:
  - [std::vector](https://en.cppreference.com/w/cpp/container/vector), fast
    read-write to element i and fast iteration operations. Slow insert
    operation.
  - [std::list](https://en.cppreference.com/w/cpp/container/list). No direct
    access to element i. Fast insert, append, splice operations.
* R: [list](http://www.r-tutor.com/r-introduction/list)
* Julia: [Array](https://docs.julialang.org/en/v1/manual/arrays/), also
    equivalent to numpy arrays.
* Fortran: [array](https://www.tutorialspoint.com/fortran/fortran_arrays.htm),
    closer to numpy arrays than python lists


## Tuples

Tuples are **short** and **immutable** containers of other data.

```
(1, 2)
("a", b")
```

Immutable means once that once created, elements cannot be added, removed or
replaced:

```python
shape = 2, 4
shape
(2, 4)
shape[1] = 4
TypeError: 'tuple' object does not support item assignment
```

## Modifying a tuple vs modifying the element of a tuple
```python
something = ["a", "b"], 4
something[0].append("c")
something
(['a', 'b', 'c'], 4)
something[0] = ["a", "b", "c"]
TypeError: 'tuple' object does not support item assignment
```

The tuple itself cannot be modified, but its elements can be if they
themselves are mutable. The container is immutable, but the contents might not
be.



Tuple make sense when:

- you need a short container with only a few elements
- the list does not need to be modified or should not be modified
- great for functions returning more than one *thing*

Beware! The following might indicate a tuple is the wrong data structure:

- the elements have no relationship (apples and oranges)
- more than four or five elements
- difficult to remember which element is what
  (is it `result[1]` I need or `result[2]?`)

## Other languages
* C++: [std::tuple](https://en.cppreference.com/w/cpp/utility/tuple)
* R: cran package [tuple](https://cran.r-project.org/web/packages/tuple/index.html)
* Julia: tuples and [named tuples](https://docs.julialang.org/en/v1/base/base/#Core.NamedTuple)
* Fortran: Nope. Nothing.


## Sets

Sets are containers where each element is *unique*:

```python
set([1, 2, 2, 3, 3])
{1, 2, 3}
```

They make sense when:

- each element in a container must be unique
- you need to solve ownership issues, e.g. which elements are in common between
  two lists? Which elements are different?

    ```python
    set(["a", "b", "c"]).symmetric_difference(["b", "c", "e"])
    {'a', 'e'}
    ```

## Other languages
* C++: [std::set](https://en.cppreference.com/w/cpp/container/set)
* R: [set functions](
     https://stat.ethz.ch/R-manual/R-devel/library/base/html/sets.html)
     that operate on a standard list.
* Julia: [Set](https://docs.julialang.org/en/v1/base/collections/#Base.Set)
* Fortran: Nope. Nothing.



## Dictionaries

Dictionaries are mappings between a key and a value (e.g. a word and its
definition).

```python
# mapping of animals to legs
{"horse": 4, "kangaroo": 2, "millipede": 1000}
```

They make sense when:

- you have pairs of data that go together:

  ```python
  # A list of pairs?? PROBABLY BAD!!
  [("horse", "mammal"), ("kangaroo", "marsupial"), ("millipede", "alien")]
  # Better?
  {"horse": "mammal", "kangaroo": "marsupial", "millipede": "alien"}
  # Or maybe?
  {"mammal": {"horse", "cow"}, "alien": {"millipede", "Jadoo"}}
  ```

- given x you want to know its y: given the name of an animal you want to know
  the number of legs.

- often used as bags of configuration options

Beware! The following might indicate a dict is the wrong data structure:

- keys are not related to each other, or values are not related to each other

  ```python
  {1: "apple", "orange": 2}
  ```

  `1` not related to `"orange"` and `2` not related to `"apple"`

- deeply nested dictionaries of dictionaries of lists of dictionaries


## Other languages
* C++: [std::map](https://en.cppreference.com/w/cpp/container/map)
* R: cran package [hash](https://cran.r-project.org/web/packages/hash/)
* Julia: [Dict](https://docs.julialang.org/en/v1/base/collections/#Base.Dict)
* Fortran: Nope. Nothing.


## Advanced data structures


- [numpy arrays](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)
  are multidimensional array of numbers
- [pandas dataframes](https://pandas.pydata.org/pandas-docs/stable/index.html")
  are collections of named 1-d arrays, i.e. excel spread-sheets on steroids
- [xarray arrays](http://xarray.pydata.org/en/stable/) are multi-dimensional
  arrays that can be indexed with rich objects, e.g. an array indexed by
  dates or by longitude and latitude, rather than by the numbers 0, 1, 2, 3.
- [xarray datasets](http://xarray.pydata.org/en/stable/) are collections of
  named [xarray arrays](http://xarray.pydata.org/en/stable/) that share some
  dimensions.
- [enum](https://docs.python.org/3/library/enum.html) represent objects that can
  only take a few *values*, e.g. colors. Often useful for configuration options.
- [networkx](https://networkx.github.io/) and
  [graph-tools](https://graph-tool.skewed.de/) implement a number of graph
  structures and graph algorithms.

## Custom data structures: Data classes

Python (= 3.7) makes it easy to create custom data structures.

```python
from typing import List, Text
from dataclasses import dataclass
@dataclass
... class MyData:
...   a_list: List[int]
...   b_string: Text = "something something"
data = MyData([1, 2])
data
MyData(a_list=[1, 2], b_string='something something')
data.a_list
[1, 2]
```

Data classes make sense when:

- you have a collections of related data that does not fit a more primitive type
- you already have a class and you don't want to write standard functions like
  `__init__`, `__repr__`, `__ge__`, etc..

Beware! The following might indicate a `dataclass` is the wrong data structure:

- you do need specialized `__init__` behaviours (just use a class)
- single huge mother of all classes that does everything (split into smaller
  specialized classes and/or stand-alone functions)
- a `dict`, `list` or `numpy` array would do the job. Everybody knows what a
  `numpy` array is and how to use it. But even your future self might not know
  how to use your very special class.


## Exploring data structures

In your own time, find out all the thing data structures can do for you:

- [list](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists),
- [set](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

As well as other standard data structures:

- [deques](https://docs.python.org/3/library/collections.html#collections.deque)
- [named tuples](https://docs.python.org/3/library/collections.html#collections.namedtuple)
- [counters](https://docs.python.org/3/library/collections.html#collections.Counter)
- [dates](https://docs.python.org/2/library/datetime.html)

All **modern** languages will have equivalents, outside of "Modern Fortran".

Don't reinvent the square wheel.


## Exercise: Digital Oxford Dictionary, the wrong way and the right way
1. Implement an oxford dictionary with two `list`s, one for words, one for
definitions:

    ```yaml
    barf: (verb) eject the contents of the stomach through the mouth
    morph: (verb) change shape as via computer animation
    scarf: (noun) a garment worn around the head or neck or shoulders for warmth
      or decoration
    snarf: (verb) make off with belongings of others
    sound: |
      (verb) emit or cause to emit sound.
      (noun) vibrations that travel through the air or another medium
    surf: |
      (verb) switch channels, on television
      (noun) waves breaking on the shore
    ```

1. Given a word, find and modify its definition
1. Do the same with a `dict`
1. Create a subset dictionary (including definitions) of words rhyming with
   "arf" using either the two-`list` or the `dict` implementation
1. If now we want to also encode "noun" and "verb", what data structure could we
   use?
1. What about when there are multiple meanings for a verb or a noun?

## Solution 1: Dictionary implemented with lists

```python
from typing import List, Text, Tuple

def modify_definition(
    word: Text, newdef: Text, words: List[Text], definitions: List[Text]
    ) -List[Text]:
    from copy import copy

    index = words.index(word)
    definitions = copy(definitions)
    definitions[index] = newdef
    return definitions

def find_rhymes(
    rhyme: Text, words: List[Text], definitions: List[Text]
    ) -Tuple[List[Text], List[Text]]:
    result_words = []
    result_definitions = []
    for word, definition in zip(words, definitions):
        if word.endswith(rhyme):
            result_words.append(word)
            result_definitions.append(definition)
    return result_words, result_definitions

def testme():

    words = ["barf", "morph", "scarf", "snarf", "sound", "surf"]
    definitions = [
        "(verb) eject the contents of the stomach through the mouth",
        "(verb) change shape as via computer animation",
        (
            "(noun) a garment worn around the head or neck or shoulders for"
            "warmth or decoration"
        ),
        "(verb) make off with belongings of others",
        (
            "(verb) emit or cause to emit sound."
            "(noun) vibrations that travel through the air or another medium"
        ),
        (
            "(verb) switch channels, on television"
            "(noun) waves breaking on the shore"
        ),
    ]

    newdefs = modify_definition("morph", "aaa", words, definitions)
    assert newdefs[1] == "aaa"

    rhymers = find_rhymes("arf", words, definitions)
    assert set(rhymers[0]) == {"barf", "scarf", "snarf"}
    assert rhymers[1][0] == definitions[0]
    assert rhymers[1][1] == definitions[2]
    assert rhymers[1][2] == definitions[3]

if __name__ == "__main__":

    # this is one way to include tests.
    # the second session will introduce a better way.
    testme()
```


## Solution 2: Dictionary implemented with a dictionary

```python
from typing import List, Text, Tuple, Mapping

def modify_definition(
    word: Text, newdef: Text, dictionary: Mapping[Text, Text]
) -List[Text]:
    from copy import copy

    result = copy(dictionary)
    result[word] = newdef
    return result

def find_rhymes(
    rhyme: Text, dictionary: Mapping[Text, Text]
) -Tuple[List[Text], List[Text]]:
    return {
        word: definition
        for word, definition in dictionary.items()
        if word.endswith(rhyme)
    }

def testme():

    dictionary = {
        "barf": "(verb) eject the contents of the stomach through the mouth",
        "morph": "(verb) change shape as via computer animation",
        "scarf": (
            "(noun) a garment worn around the head or neck or shoulders for"
            "warmth or decoration"
        ),
        "snarf": "(verb) make off with belongings of others",
        "sound": (
            "(verb) emit or cause to emit sound."
            "(noun) vibrations that travel through the air or another medium"
        ),
        "surf": (
            "(verb) switch channels, on television"
            "(noun) waves breaking on the shore"
        ),
    }

    newdict = modify_definition("morph", "aaa", dictionary)
    assert newdict["morph"] == "aaa"

    rhymers = find_rhymes("arf", dictionary)
    assert set(rhymers) == {"barf", "scarf", "snarf"}
    for word in {"barf", "scarf", "snarf"}:
        assert rhymers[word] == dictionary[word]

if __name__ == "__main__":

    testme()
```




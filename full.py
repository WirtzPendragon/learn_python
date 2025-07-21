##################################################
# 1. Primitive Datatypes and Operators
##################################################

# You have numbers
3 # => 3

# Math is what you would expect
1 + 1    # => 2
8 - 1    # => 7
10 * 2   # => 20
35 / 5   # => 7.0

# Floor division rounds towards negative infinity
5 // 3      # => 1
-5 // 3     # => -2
5.0 // 3.0  # => 1.0 # works also on floats too
-5.0 // 3.0 # => -2.0

# The result of division is always a float
10.0 / 3 # => 3.3333333333333335

# Modulo operation
7 % 3  # => 1
# i % j have the same sign as j, unlike C
-7 % 3 # => 2

# Exponentation (x**y, x to the yth power)
2**3 # => 8

# Enforce precendence with parenthess
1 + 3 * 2   # => 7
(1 + 3) * 2 # => 8

# Boolean values are primitives (Note: the capitalization)
True  # => True
False # => False

# negate with note
not True  # => False
not False # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False # => False
False or True  # => True

# True and False are actually 1 and 0 but with different keywords
True + True # => 2
True * 8    # => 8
False - 5   # => -5
# Comparison operators look at the numerical value of True and False
0 == False  # => True
2 > True    # => True
2 == True   # => False
-5 != False # => true

# None, 0, and emoty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0)     # => False
bool("")    # => False
bool([])    # => False
bool({})    # => False
bool(())    # => False
bool(set()) # => False
bool(4)     # => True
bool(-6)    # => True

# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
bool(0)  # => False
bool(2)  # => True
0 and 2  # => 0
bool(-5) # => True
bool(2)  # => True
-5 or 0  # => -5

# Equality is ==
1 == 1 # => True
2 == 1 # => False

# Inequality is !=
1 != 1 # => False
2 != 1 # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3 # => True
2 < 3 and 3 < 2 # => False
# Chaining makes this look nicer
1 < 2 < 3 # => True
2 < 3 < 2 # => False

# (is vs. ==) is checks if two variables refer to the same object, but checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4] # Point a at a new list, [1, 2, 3, 4]
b = a            # Point b at what a is pointing to
b is a           # => True, a abd b refer to the same object
b == a           # => True, a's and b's objects are equal
b = [1, 2, 3, 4] # Point a b at new list, [1, 2, 3, 4] b is a           # => False, a abd b di not refer to the same object b == a           # => True, a's and b's objects are equal # Strings can be added to "Hello " + "world!" # => "Hello world!"
# String literals (but not variabels) can be concatenated without using '+'
"Hello " "world!"   # => "Hello world!"

# A string can be treated like a list of characters
"Hello world!"[0] # => 'H'

# You can find the length of a string
len("This is a string") # => 16

# Since Python 3.6, you can use f-strings to formatted string literrals.
name = "Reiko"
f"she said her name is{name}." # => "She said her name is Reiko"
# Any valid Python expression inside these braces is returned to the string.
f"{name} is {len(name)} characters long." # => "Reiko is 5 characters long."

# None is an object
None # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
"etc" is None # => False
None is None  # => True

##################################################
## 2. Variables and Collections
##################################################

# Python has a print function
print("I'm Python. Nice to meet you!") # => I'm Python. Nice to meet you!

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!") # => Hello, World!

# Simple way to get input data from console
input_string_var = input("Enter some data: ") # Returns the data as a string

# There are no declarations, only assignments.
# Convertion in naming variables is snake_case style
some_var = 5
some_var # => 5

# Accessing a previosly unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
#some_unknown_var # Raises a NameError

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yay!" if 0 > 1 else "nay!" # => "nay!"

# Lists store sequences
li = []
# You cam start with a prefield list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.apppend(1)  # li is now [1]
li.apppend(2)  # li is now [1, 2]
li.apppend(4)  # li is now [1, 2, 4]
li.apppend(3)  # li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()
# Let's put it back
li.append(3) # li is now [1, 2, 4] again

# Access a list like you would any array
li[0]  # => 1
# Look at the last element
li[-1] # => 3

# Looking out of bounds is an IndexError
li[4] # Raises an IndexError

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It,s a closed/open range for you mathy types.)
li[1:3]    # Return list from index 1 to 3 => [2, 4]
li[2:]     # Return list satrting from index 2 => [4, 3]
li[:3]     # Return list from beginning until index 3 => [1, 2, 4]
li[::2]    # Return list selecting elements with a strp size of 2 => [1, 4]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:] # => li2 = [1, 2, 3, 4] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2] # li is now [1, 2, 3]

# Remove first occurance of a value
li.remove(2) # li is now [1, 3]
li.remove(2) # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2) # => li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2) # => 1
li.index(4) # => Raises a ValueError as 4 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified.
li + other_li # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li) # => Now li is [1, 2, 3, 4, 5, 6]

# Check fr existence in a list with "in"
1 in li # => True

# Examine the length with "len()"
len(li) # => 6

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]     # => 1
tup[0] = 3 # Raises a TypeError 

# Note that a tuple of length one has to have coma after the last element but
# tuples of other lengths, even zero, do not.
type((1))  # => <class 'int'>
type((1,)) # => <class 'tuple'>
type(())   # => <class 'tuple'>

# You can do most of the list operations on tuples too
len(tup)        # => 3
tup + (4, 5, 6) # => (1, 2, 3, 4, 5, 6)
tup[:2]         # => (1, 2)
2 in tup        # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3) # a is now 1, b is now 2, c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4) # a is now 1, b is now [2, 3], and c is now 4
# Tuples are created by default if you leave out the parenteses
d, e, f = 4, 5, 6 # tuple 4, 5, 6 is unpacked into variables d, e, and f
# respectively such that d = 4, e = 5, f = 6
# Now look how easy it is to swap two values
e, d = d, e # d is now 5, and e is now 4

# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be imutable types. This is to ensure that
# the key can be converted to a constant hash value for quick looks-up.
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"} # => Yield a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}  # Values can be of any type, however.

# Look up values with []
filled_dict["one"] # => 1

# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values()) # => [3, 2, 1] in Python <3.7
list(filled_dict.values()) # => [1, 2, 3] in Python 3.7+

# Check for existance of keys in a dictionary with "in"
"one" in filled_dict # => True
1 in filled_dict     # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"] # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")     # => 1
filled_dict.get("four")    # => None
# The get method supports a default a dictionary only if the given key isn't present
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4) # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault({"five", 5}) # filled_dict["five"] is set to 5
filled_dict.setdefault({"five", 6}) # filled_dict["five"] is still 5

# Adding to a dictionary
filled_dict.update({"four": 4}) # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"] # Removes the key "one" from filled dict

# From Python 3.5 you can also use the additional unpacking options
{"a": 1, **{"b": 2}} # => {'a': 1, 'b': 2}
{"a": 1, **{"a": 2}} # => {'a': 2}

# Sets store ... well sets
empty_set = set()
# Initialize a set with a bunch of values.
some_set = {1, 1, 2, 2, 3, 4} # some_set is now {1, 2, 3, 4}

# Similiar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1} # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# Add one more item to the set
filled_set = some_set
filled_set.add(5) # filled_set is now {1, 2, 3 ,4 ,5}
# Sets do not have duplicate elements
filled_set.add(5) # it remains as before {1, 2, 3, 4, 5}

# Do set intersection with $
other_set = {3, 4, 5, 6}
filled_set & other_set # => {3, 4, 5}

# Do set union with |
filled_set | other_set # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5} # => {1, 4}

# Do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5} # => {1, 4, 5}

# Check if set on the left is superset of set on the right
{1, 2} >= {1, 2, 3} # False

# Check if set on the left is a subset of set the right
{1, 2} <= {1, 2, 3} # True

# Check for existence in a set with in
2 in filled_set  # True
10 in filled_set # False

# Make a one layer deep copy
filled_set = some_set.copy() # filled_set is {1, 2, 3, 4, 5}
filled_set is some_set       # => False


##################################################
## 3. Control Flow and Iterables
##################################################

# Let's just make a variable
some_var = 5

# Here is an if statement. Indentation is significant in Python!
# Convention is to use four spaces, not tabs.
# This prints "some_vas is smalles than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10: # This elif clause is optional.
    print("some_var is smaller than 10.")
else:               # This elif clause is optional.                    
    print("some_var is indeed 10.")

# Match/Case - Introduced in Python 3.10
# It compares a value agains multiple patterns and executes the matching case block.

command = "run"

match command:
    case "run":
        print("The robot started to run 🏃‍♂️")
    case "speak" | "say_hi": # multiple options (OR pattern)
        print("The robot said hi 🗣️")
    case code if command.isdigit(): # conditional
        print(f"The robot execute code: {code}")
    case _: # _ is a wildcard that never fails (like default/else)
        print("Invalid command ❌")

# Output: "the robot started to run 🏃‍♂️"

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))
    
"""
"range(number)" returns an iterable of numbers
from zero up to (but excluding) the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
points:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""
Loop over a list to retrive both the index and the value of each list item:
    0 dog
    1 cat
    2 mouse
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1 # Shorthand for x = x + 1

# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                    # Refrain from this, provide a recovery (next example).
except (TypeError, NameError):
    pass                    # Multiple exceptions can be processed jointly.
else:                       # Optional clause to the try/except block. Must follow
                            # all except blocks.
    print("All good!")      # Runs only if the code in try raises no exceptions
finally:                    # Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Writing to a file
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w") as file:
    file.write(str(contents))           # writes a string to a file

import json
with open("myfile2.txt", "w") as file:
    file.write(json.dumps(contents))    # writes an object to a file

# Reading from a file
with open("myfile1.txt") as file:
    contents = file.read()              # reads a string from a file
print(contents)
# print {"aa": 12, "bb": 21}

with open("myfile2.txt", "r") as file:
    contents = json.load(file)          # reads a json object from a file
print(contents)
# print: {"aa": 12, "bb": 21}

# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => dict_keys(['one', 'two', 'three']). This is an object
                    # that implements our Iterable interface.

# We can loop over it.
for i in our_iterable:
    print(i) # Prints one, two, three

# However we cannot address elements by index.
our_iterable[1] # Raises a TypeError

# An iterable is an object that knows how to create an iterator.
our_iterator = iter(our_iterable)

# Our iterator is an object that can remember the state as we traverse through
# it. We get the next object with "next()".
next(our_iterator) # => "one"

# It maintains state as we iterate.
next(our_iterator) # => "two"
next(our_iterator) # => "three"

# After the iterator has returned all of its data, it raise a
# StopIteration exception
next(our_iterator) # Raises StopIteration

# We can also loop over it, in fact "for" does this implicitly!
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i) # Prints one, two, three

# You can grab all the elements of an iterable or iterator by call of list().
list(our_iterable) # => Returns ["one", "two", "three"]
list(our_iterator) # => Returns [] because state is saved
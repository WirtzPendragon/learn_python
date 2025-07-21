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
b = [1, 2, 3, 4] # Point a b at new list, [1, 2, 3, 4]
b is a           # => False, a abd b di not refer to the same object
b == a           # => True, a's and b's objects are equal

# Strings can be added to
"Hello " + "world!" # => "Hello world!"
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
# Lambda
# It is a small anonymous function. Syntax: lambda arguments: expression
# Syntax:  lambda arguments: expression
add = lambda x,y: x+y


numbers = [1,2,3,4,5]

# Map Function
# It applies a given function to each item of an iterable (like a list) and returns an iterator.
squares = map(lambda x: x * x, numbers)
print(list(squares))


# Filter Function
# It constructs an iterator from elements of an iterable for which a function returns True.
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

# Reduce Function
# It applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
from functools import reduce

# Example 1: Sum of numbers
sum_of_numbers= reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# Example 2: Product of numbers
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)

# Example 3: Find maximum number
maximum_number = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum_number)
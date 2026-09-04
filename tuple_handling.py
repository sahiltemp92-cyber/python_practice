test_tuple = (1,2,3,4,5,"sahil")
"""
List and Tuple difference are as follows:
1.List is mutable . Tuple is immutable.
2.List is slower than tuple.
3.List takes more memory than tuple.
4.List is more flexible than tuple.
5.List is more powerful than tuple.
6.List is more flexible than tuple.
"""

print(test_tuple)
print(test_tuple[2]) # Access element at index 2
print(test_tuple[2:5]) # Slicing
print(test_tuple[::-1]) # Reverse
print(len(test_tuple)) # Length
print(test_tuple.count("sahil")) # Count
print(test_tuple.index("sahil")) # Index
print("sahil" in test_tuple) # Membership
print(sorted(test_tuple)) # Sort
print(sorted(test_tuple, reverse=True)) # Sort reverse
print(list(test_tuple)) # Convert to list
print(tuple(test_tuple)) # Convert to tuple
print(tuple(test_tuple[::-1])) # Reverse tuple
print(tuple(sorted(test_tuple))) # Sort tuple
print(tuple(sorted(test_tuple, reverse=True))) # Sort tuple reverse
print(tuple(sorted(test_tuple))[::-1]) # Sort tuple reverse
print(tuple(sorted(test_tuple))[::-1][::-1]) # Sort tuple reverse reverse
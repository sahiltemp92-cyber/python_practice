numbers = [1,2,3,4,5,"sahil"]


# Add element to list
numbers.append("python") # Add to end
numbers.insert(2,"automation") # Add at specific position

# Remove element from list
numbers.remove("sahil") # Remove by value
numbers.pop() # Remove last element
numbers.pop(2) # Remove at specific position
del numbers[2] # Remove at specific position

# Remove all elements from list
numbers.clear() # Remove all elements

# Check if element exists in list
print("sahil" in numbers) # Check if element exists

# Count occurrences of element in list
print(numbers.count("sahil")) # Count occurrences

# Sort list
numbers.sort() # Sort in ascending order
numbers.sort(reverse=True) # Sort in descending order

# Reverse list
numbers.reverse() # Reverse the list

# Copy list
numbers.copy() # Create a copy of the list

# Extend list
numbers.extend([6,7,8,9,10]) # Extend the list with another list

# Index of element
print(numbers.index("sahil")) # Get the index of the element

# Length of list
print(len(numbers)) # Get the length of the list

# Membership testing
print("sahil" in numbers) # Check if element exists

# Slicing
print(numbers[2:5]) # Get elements from index 2 to 5
print(numbers[:5]) # Get first 5 elements
print(numbers[5:]) # Get elements from index 5 to end

# List comprehension
squares = [x * x for x in numbers]
print(squares)

# Nested list
nested_list = [1,2,3,[4,5,6,[7,8,9]]]
print(nested_list[3][2][0]) # Access nested elements

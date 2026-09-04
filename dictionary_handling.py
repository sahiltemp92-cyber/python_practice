dict = {
    "name" : "Sahil",
    "age" : 25,
    "gender" : "Male",
    "city" : "Mumbai"
}

print(dict)
print(dict["name"])
print(dict["age"])
print(dict["gender"])
print(dict["city"])

# Add element to dictionary
dict["email"] = "[EMAIL_ADDRESS]" # Add new key-value pair

# Update element in dictionary
dict["age"] = 26 # Update existing value

# Remove element from dictionary
del dict["city"] # Remove key-value pair
dict.pop("gender") # Remove key-value pair
dict.popitem() # Remove last key-value pair

# Remove all elements from dictionary
dict.clear() # Remove all key-value pairs

# Get the value of a key
print(dict.get("name")) # Get value of name

# Get all keys
print(dict.keys()) # Get all keys

# Get all values
print(dict.values()) # Get all values

# Get all key-value pairs
print(dict.items()) # Get all key-value pairs

# Check if key exists in dictionary
print("name" in dict) # Check if key exists

# Length of dictionary
print(len(dict)) # Get the length of the dictionary

# Copy of dictionary
dict.copy() # Create a copy of the dictionary

# Nested dictionary
nested_dict = {
    "name" : "Sahil",
    "age" : 25,
    "address" : {
        "city" : "Mumbai",
        "state" : "Maharashtra"
    }
}
print(nested_dict["address"]["city"]) # Access nested dictionary

# Dictionary comprehension
doubled_dict = {x: x * 2 for x in range(5)}
print(doubled_dict) # Create dictionary with doubled values

# Iterate over dictionary
for key, value in dict.items():
    print(key, value) # Iterate over key-value pairs
    
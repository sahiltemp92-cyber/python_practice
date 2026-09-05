numbers = [1,5,6,1,6,4,2,9,8,1,0,6,5,8]

def triplet_sort(arr):
    result = []
    # Process the list in chunks of 3
    for i in range(0, len(arr), 3):
        triplet = arr[i:i+3]
        result.extend(sorted(triplet))
    return result

# Example usage
expected = triplet_sort(numbers)
print(expected)
# Input : [1, 5, 6, 1, 6, 4, 2, 9, 8, 1, 0, 6, 5, 8]
# Output: [1, 5, 6, 1, 4, 6, 2, 8, 9, 0, 1, 6, 5, 8]


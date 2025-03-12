# Function to count occurrences using hashing

def count_occurrences(arr):
    hash_table = {}  # Dictionary as a hash table

    for num in arr:
        if num in hash_table:
            hash_table[num] += 1  # Increment count if already present
        else:
            hash_table[num] = 1  # Initialize count

    return hash_table


arr = [1, 4, 2, 3, 4, 12]
result = count_occurrences(arr)
print(result)

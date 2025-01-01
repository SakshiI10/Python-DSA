def find_max(arr, low, high):
    # Base case: If the array contains only one element
    if low == high:
        return arr[low]
    
    # Find the middle of the array
    mid = (low + high) // 2
    
    # Recursively find the maximum in the left half and right half
    max_left = find_max(arr, low, mid)
    max_right = find_max(arr, mid + 1, high)
    
    # Return the larger of the two
    return max(max_left, max_right)

if __name__ == "__main__":
    arr = [3, 5, 1, 9, 2, 8]
    result = find_max(arr, 0, len(arr) - 1)
    print("Maximum element:", result)

# Time Complexity: O(n)
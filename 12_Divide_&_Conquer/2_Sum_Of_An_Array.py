def find_sum(arr, low, high):
    # Base case: If the array contains only one element
    if low == high:
        return arr[low]
    
    # Find the middle of the array
    mid = (low + high) // 2
    
    # Recursively find the maximum in the left half and right half
    left_sum = find_sum(arr, low, mid)
    right_sum = find_sum(arr, mid + 1, high)
    
    # Return the larger of the two
    return left_sum + right_sum

if __name__ == "__main__":
    arr = [3, 5, 1, 9, 2, 8]
    result = find_sum(arr, 0, len(arr) - 1)
    print("Sum of elements:", result)

# Time Complexity: O(n)
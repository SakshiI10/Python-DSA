def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return start  # Correct position to insert key

def binary_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        pos = binary_search(arr, key, 0, i - 1)  # Find the correct position

        # Shift elements to make space for key
        arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]

    return arr  # Return sorted array

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = binary_insertion_sort(arr)
print("Sorted array:", sorted_arr)

# Time Complexity:
# Best Case: 
# No of comparisons: O(log n) per element
# No of swaps: O(nlogn)

# Average Case:
# No of comparisons: O(log n) per element
# No of swaps: O(n^2)

# Worst Case: 
# No of comparisons: O(log n) per element
# No of swaps: O(n^2)

# Space Complexity: O(1)
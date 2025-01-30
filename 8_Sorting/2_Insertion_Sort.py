def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):  # Start from the second element
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place the key at its correct position

arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("Sorted array:", arr)

# Time Complexity:
# Best Case (Sorted Array): O(n)
# Average Case: O(n²)
# Worst Case (Reverse Sorted): O(n²)
# Space Complexity: O(1) 

# Is Insertion sort in place? Yes
# Is Insertion sort stable? Yes
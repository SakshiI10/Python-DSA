def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                swapped = True
        if not swapped:  # If no swaps happened, the array is already sorted
            break

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)

# Time Complexities:
# Best: O(n)
# Average: O(n^2) 
# Worst: O(n^2)
# Space: O(1)

# Is Bubble sort in place? Yes
# Is Bubble sort stable? Yes
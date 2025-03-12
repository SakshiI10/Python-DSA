def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Assume the current position is the minimum
        min_index = i
        
        # Find the minimum element in the remaining unsorted part
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array:", arr)

# Time Complexity:
# Best Case: O(n²)
# Worst Case: O(n²)
# Average Case: O(n²)

# Space Complexity: # O(1) 

# Is Selection sort in place? Yes
# Is Selection sort stable? No
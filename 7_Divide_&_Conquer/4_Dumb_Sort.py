def dumb_sort(a, i, j):
    # Base case: if i equals j, the array is sorted
    if i == j:
        return
    
    # Iterate from k=i+1 to j
    for k in range(i + 1, j+1):
        # Compare a[k-1] and a[k] and swap if necessary
        if a[k - 1] > a[k]:
            a[k - 1], a[k] = a[k], a[k - 1]
    
    # Recursively call my_sort to sort the subarray
    dumb_sort(a, i, j - 1)

# Example usage:
arr = [5, 3, 8, 4, 2]
dumb_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

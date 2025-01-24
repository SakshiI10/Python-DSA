def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2
        
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        
        # Recursive call on each half
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
print("Original Array: ",arr)
merge_sort(arr)
print("Sorted array:", arr)

# Overall Time Complexity: The overall time complexity for merge sort is the sum of dividing, sorting, and merging.

# Divide: 𝑂(log⁡2(𝑛))
# Sort: 𝑂(𝑛⋅log⁡2(𝑛))
# Merge: 𝑂(𝑛⋅log⁡2(𝑛))

# Thus, the overall time complexity of merge sort is: 𝑇(𝑛)=𝑂(𝑛⋅log⁡2(𝑛))
          
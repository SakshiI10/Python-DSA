def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max) with last element
        heapify(arr, i, 0)  # Heapify the reduced heap

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)

# Time Complexity:
# Building the Max Heap: O(n)
# Heapifying the root for each element: O(log n)
# Total time complexity: O(n log n) (since we heapify n times, each taking O(log n))

# Space Complexity: O(1) 
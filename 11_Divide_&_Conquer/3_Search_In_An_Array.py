def search(arr, low, high, value):
    # Base case: If low equals high, check if the value matches the element at that index
    if low == high:
        if arr[low] == value:  # or arr[high], since low == high
            return True
        else:
            return False
    
    # Calculate mid-point to divide the array
    mid = (low + high) // 2
    
    # Recursively search the left and right halves of the array
    return search(arr, low, mid, value) or search(arr, mid + 1, high, value)

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
value = 7
found = search(arr, 0, len(arr) - 1, value)

if found:
    print(f"Value {value} found in the array.")
else:
    print(f"Value {value} not found in the array.")

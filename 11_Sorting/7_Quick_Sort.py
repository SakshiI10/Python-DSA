def partition(array, low, high):
    # Choose the leftmost element as the pivot
    pivot = array[low]
    i = low + 1   
    j = high
   
    while i <= j:
        # Find the first element greater than pivot
        while i <= j and array[i] <= pivot:
            i += 1

        # Find the first element smaller than or equal to pivot
        while i <= j and array[j] > pivot:
            j -= 1

        # Swap elements if pointers haven't crossed
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    # Swap the pivot with the element at j (final pivot position)
    array[low], array[j] = array[j], array[low]

    # Return the pivot position
    return j

def quicksort(array, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(array, low, high)

        # Recursive call on the left of the pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of the pivot
        quicksort(array, pi + 1, high)

if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    print("Original Array:", array)

    # Function call
    quicksort(array, 0, len(array) - 1)

    # Print the sorted array
    print("\nSorted Array:", array)


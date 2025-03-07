# Using a single pointer
def reverse(arr, i=0):
    n = len(arr)
    if i >= n // 2:  
        return arr

    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]  
    return reverse(arr, i + 1)  

# Using two pointers
def reverse2(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1  
    if l >= r:  
        return arr  

    arr[l], arr[r] = arr[r], arr[l]  
    return reverse2(arr, l + 1, r - 1)  

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
print(reverse(arr1))  
print(reverse2(arr2))  

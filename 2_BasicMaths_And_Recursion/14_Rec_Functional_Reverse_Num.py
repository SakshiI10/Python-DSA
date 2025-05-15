# Using a single pointer
def reverse(arr, i=0):
    n=len(arr)
    i=0
    while i < n//2:
        arr[i], arr[n-1-i]=arr[n-1-i], arr[i]
        i += 1
    return arr 

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
 
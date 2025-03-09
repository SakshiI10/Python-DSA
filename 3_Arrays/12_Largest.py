def largest(arr):
    n=len(arr)
    arr.sort()
    return arr[n-1]

def slargest(arr):
    n=len(arr)
    arr.sort()
    return arr[n-2]

arr=[1, 9, 5, 3, 7, 5]
print(largest(arr))
print(slargest(arr))

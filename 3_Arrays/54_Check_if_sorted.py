def check(arr):
    result=arr[:]   # Create a copy of the original list
    arr.sort()
    if result==arr:
        print("Sorted")
    else:
        print("Not sorted")

arr=[1, 9, 5, 4, 3, 7]
arr2=[1, 2, 3, 4, 5, 6]
check(arr)
check(arr2)
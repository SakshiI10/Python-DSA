'''
Pitsy needs help with the given task by her teacher. The task is to divide an array into two sub-array (left and right) containing n/2 elements each and do the sum of the subarrays and then multiply both the subarrays.
Note: If the length of the array is odd then the right half will contain one element more than the left half.

Input : arr[ ] = {1, 2, 3, 4}
Output : 21'''

def multiply (arr, n) : 
    divide = n//2
    sum1 = sum(arr[:divide])
    sum2 = sum(arr[divide:])
    result=sum1*sum2
    return result

arr = [1, 2, 3, 4]
n = len(arr)
print(multiply(arr, n))  # Output: 21

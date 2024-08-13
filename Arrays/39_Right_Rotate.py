'''
Given an array arr, rotate the array by one position in clock-wise direction.
Input: arr = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]'''

def left_rotate(arr, d):
    n = len(arr)
    d = d % n  
    return arr[d:] + arr[:d]

def right_rotate(arr, d):
    n = len(arr)
    d = d % n  
    return arr[-d:] + arr[:-d]

arr = [1, 2, 3, 4, 5]
d = 1

left_rotated_arr = left_rotate(arr, d)
right_rotated_arr = right_rotate(arr, d)

print(f"Original array: {arr}")
print(f"Array after left rotation by {d}: {left_rotated_arr}")
print(f"Array after right rotation by {d}: {right_rotated_arr}")

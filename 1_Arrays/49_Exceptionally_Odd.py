'''
Given an array of N positive integers where all numbers occur even number of times except one number which occurs odd number of times. Find the exceptional number.

Input: N = 7
Arr[] = {1, 2, 3, 2, 3, 1, 3}
Output: 3 '''

def find_odd_occurrence(arr):
    frequency = {}

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num, count in frequency.items():
        if count % 2 != 0:
            return num

arr1 = [1, 2, 3, 2, 3, 1, 3]
print(find_odd_occurrence(arr1))  # Output: 3   

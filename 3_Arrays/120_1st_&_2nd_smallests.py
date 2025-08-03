'''
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. If the smallest and second smallest do not exist, return -1.

Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3 '''

class Solution:
    def minAnd2ndMin(self, arr):
        unique_list = list(set(arr))
        unique_list.sort()

        if len(unique_list) < 2:
            return (-1, -1)  
        else:
            return (unique_list[0], unique_list[1])
        
sol = Solution()
arr = [2, 4, 3, 5, 6]
print(sol.minAnd2ndMin(arr))  

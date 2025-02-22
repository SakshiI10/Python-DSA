'''
Given an even sized array arr[], where each consecutive pair of elements represents a height with two fields: feet and inches. Find the maximum height, where the height is calculated by converting feet to inches and adding the inches.

Input: arr[] = [1, 2, 2, 1] 
Output: 25'''

class Solution:
    def findMax(self, arr):
        max_height=0
        n=len(arr)

        for i in range(0, n, 2):
            feet=arr[i]
            inches=arr[i+1]
            total_inches = feet * 12 + inches
            
            if total_inches > max_height:
                max_height = total_inches
        
        return max_height

sol = Solution()    
arr1 = [1, 2, 2, 1]
print(sol.findMax(arr1))  # Expected Output: 25
arr2 = [3, 2, 2, 3, 1, 2]
print(sol.findMax(arr2))  # Expected Output: 38

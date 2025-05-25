'''You are given an array arr and an integer k. In one operation you can choose any element of array and decrease its value by k. You need find the minimum number of operation such that all the elements in the array becomes less or equal to k.

Examples:

Input: arr[] = [5, 3, 2, 6, 8] and k = 5
Output: 2'''

class Solution:
    def reducingWalls(self, arr, k):
        count = 0
        
        for i in range(len(arr)):
            if arr[i] > k:
                count += 1
        return count

sol=Solution()
arr = [5, 3, 2, 6, 8]   
print(sol.reducingWalls(arr, 5))  
arr2 = [2, 6, 4, 8, 1, 6]   
print(sol.reducingWalls(arr2, 5))  

'''
You are given an array arr[] having unique elements. Your task is to return the type of array.
Note: The array can be categorized into ascending, descending, descending rotated and ascending rotated followed by:

Return 1 if the array is in ascending order
Return 2 if the array is in descending order
Return 3 if the array is in descending rotated order
Return 4 if the array is in ascending rotated order
Examples:

Input: arr[] = [2, 1, 5, 4, 3]
Output: 3'''

class Solution:
    def maxNtype(self, arr):
        n = len(arr)
        asc = desc = True

        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                asc = False
            if arr[i] > arr[i - 1]:
                desc = False

        if asc:
            return 1
        if desc:
            return 2

        # Count breaks in ascending and descending pattern
        asc_breaks = 0
        desc_breaks = 0
        for i in range(n):
            if arr[i] > arr[(i + 1) % n]:
                asc_breaks += 1
            if arr[i] < arr[(i + 1) % n]:
                desc_breaks += 1

        if asc_breaks == 1:
            return 4 
        if desc_breaks == 1:
            return 3  
        
        return -1 

sol=Solution()
arr=[2, 1, 5, 4, 3]
print(sol.maxNtype(arr))  
'''
Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array. If both elements have the same frequency, then return the smaller element.
Note:  We need to return the element, not its count.

Input:
N = 11
arr[] = {1,1,2,2,3,3,4,4,4,4,5}
x = 4, y = 5
Output: 4'''

class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        count_x, count_y = 0, 0
        
        for i in range(n):
            if arr[i] == x:
                count_x += 1
            elif arr[i] == y:
                count_y += 1
                
        if count_x > count_y:
            return x
        elif count_x < count_y:
            return y
        else:
            return min(x, y)
        
sol=Solution()
arr=[1,1,2,2,3,3,4,4,4,4,5]
x, y = 4, 5
print(sol.majorityWins(arr, len(arr), x, y))
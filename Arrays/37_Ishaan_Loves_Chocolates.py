'''
As we know, Ishaan has a love for chocolates. He has bought a huge chocolate bar that contains N chocolate squares. Each of the squares has a tastiness level which is denoted by an array A[].
Ishaan can eat the first or the last square of the chocolate at once. Ishaan has a sister who loves chocolates too and she demands the last chocolate square. Now, Ishaan being greedy eats the more tasty square first. 
Determine the tastiness level of the square which his sister gets.

Input : arr[] = {5, 3, 1, 6, 9}
Output : 1'''

from typing import List

class Solution:
    def chocolates(self, n, arr):
        left, right = 0, n - 1
        
        while left < right:
            if arr[left] >= arr[right]:
                left += 1
            else:
                right -= 1
                
        return arr[left]

sol = Solution()
arr = [5, 3, 1, 6, 9]
result = sol.chocolates(len(arr), arr)
print(result)  

'''
Given an array arr[] of integers, find the number of pairs whose XOR is odd in the array.

Input: arr[] = [1, 2, 3]
Output: 2

Input: arr[] = [1, 2]
Output: 1'''

class Solution:

    def countOddXorPairs(self, arr):
        odd_count = 0
        even_count = 0

        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        return odd_count * even_count
    
sol=Solution()
arr=[1, 2, 3]
print(sol.countOddXorPairs(arr))
 
'''
Input: N = 3
arr = {40, 50, 90}
Output: 1
Explanation: One such number is 405090.'''

class Solution:
    def isPossible(self, N, arr):
        digit_sum = 0
        for num in arr:
            for digit in str(num):
                digit_sum += int(digit) 
        
        if digit_sum % 3 == 0:
            return 1 
        else:
            return 0
        
sol=Solution()
arr = [40, 50, 60]
print(sol.isPossible(len(arr), arr))
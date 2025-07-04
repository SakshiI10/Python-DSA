'''You are given an integer n. You need to convert all zeroes of n to 5.

Input: n = 1004
Output: 1554 '''

class Solution:
    def convertFive(self, n):
        digits = list(str(n))
        found_zero = False
        
        for i in range(len(digits)):
            if digits[i] == '0':
                digits[i] = '5'
                found_zero = True
        
        if found_zero:
            return int(''.join(digits))
        else:
            return n

sol = Solution()
print(sol.convertFive(1004))  # Output: 1554
print(sol.convertFive(121))   # Output: 121

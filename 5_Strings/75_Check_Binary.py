'''
Given a binary string S of 0 and 1, check if the given string is valid or not. The given string is valid when there is no zero is present in between 1s.

Input:
S = "100"
Output: VALID'''

class Solution:
    def checkBinary (self, s):
        first_one = s.find('1')
        last_one = s.rfind('1')

        if '0' in s[first_one:last_one + 1]:
            return 'INVALID'
        return 'VALID'
    
sol=Solution()
S='100'
print(sol.checkBinary(S))
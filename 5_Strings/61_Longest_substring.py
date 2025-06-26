'''
Given a function that takes a binary string. The task is to return the longest size of contiguous substring containing only ‘1’.

Input:
2
110
11101110
Output:
2
3
'''

class Solution:
    def maxlength(self, s):
        max_len = 0
        length = 0

        for char in s:
            if char == '1':
                length += 1
                max_len = max(max_len, length)
            else:
                length = 0 
        
        return max_len

sol=Solution()
s='11101110'
print(sol.maxlength(s))
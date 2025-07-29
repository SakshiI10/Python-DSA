'''
Given two strings s1 and s2. Modify both the strings such that all the common characters of s1 and s2 are to be removed and the uncommon characters of s1 and s2 are to be concatenated.
Note: If all characters are removed print -1.

Input:
s1 = aacdb
s2 = gafd
Output: cbgf'''

class Solution:
    def concatenatedString(self,s1,s2):
        common=set(s1)&set(s2)
        res = ''

        for char in s1:
            if char not in common:
                res += char
        
        for char in s2:
            if char not in common:
                res += char

        if not res:
            return "-1"
        return ''.join(res)
    
sol=Solution()
s1 = 'aacdb'
s2 = 'gafd'
print(sol.concatenatedString(s1, s2))

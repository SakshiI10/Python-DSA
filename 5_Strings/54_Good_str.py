'''
Input: s = "aaa"
Output: NO
Explanation: distance between 'a' and 'a' is not 1.
Example 2:

Input: s = "cbc"
Output: YES
Explanation: distance between 'b' and 'c' is 1.
'''

class Solution:
    def isGoodString(self, s):
        n = len(s)
        
        if n == 1:
            return "YES"
        
        for i in range(1, n):
            dist = abs(ord(s[i]) - ord(s[i-1]))
            if min(dist, 26 - dist) != 1:
                return "NO"
        
        return "YES"
    
sol= Solution()
s = "cbc"
print(sol.isGoodString(s))
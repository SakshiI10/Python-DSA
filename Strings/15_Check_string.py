'''
Given a string, check if all its characters are the same or not.

Input:
s = "geeks"
Output: False'''

class Solution:
    def check(self, s: str) -> bool:
        n = len(s)
        
        if n == 0 or n == 1:
            return True
        
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                return False
        return True

sol = Solution()
print(sol.check("geeks"))  # Output: False
print(sol.check("gggg"))   # Output: True

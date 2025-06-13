'''
Given a string, say S, print it in reverse manner eliminating the repeated characters and spaces.

Input: S = "GEEKS FOR GEEKS"
Output: "SKEGROF"'''

class Solution:
    def reverseString(self, s):
        res=[]
        
        for char in reversed(s):
            if char not in res and char != ' ':
                res.append(char)
        
        return ''.join(res)
        

sol = Solution()
print(sol.reverseString("GEEKS FOR GEEKS"))  # Output: "SKEGROF"

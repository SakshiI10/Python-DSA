'''
Given a string, say S, print it in reverse manner eliminating the repeated characters and spaces.

Input: S = "GEEKS FOR GEEKS"
Output: "SKEGROF"'''

class Solution:
    def reverseString(self, s):
        seen = set()
        result = []
        
        for char in reversed(s):
            if char != ' ' and char not in seen:
                seen.add(char)
                result.append(char)
        
        return ''.join(result)

sol = Solution()
print(sol.reverseString("GEEKS FOR GEEKS"))  # Output: "SKEGROF"

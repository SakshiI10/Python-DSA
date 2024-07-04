''' 
Given a string, remove spaces from it. 

Input:
S = "geeks  for geeks"
Output: geeksforgeeks
Explanation: All the spaces have been 
removed.'''

class Solution:
    def modify(self, s: str) -> str:
        result = ""
        for char in s:
            if char != ' ':
                result += char
        return result

sol = Solution()
s = "geeks  for geeks"
print(sol.modify(s))  # Output should be "geeksforgeeks"
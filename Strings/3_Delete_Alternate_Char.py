''' 
Given a string S as input. Delete the characters at odd indices of the string.
Input: S = "Geeks"
Output: "Ges" 
Explanation: Deleted "e" at index 1
and "k" at index 3.'''

class Solution:
    def delAlternate(self, S):
        # Slicing the string to take characters at even indices
        return S[::2]

sol = Solution()
print(sol.delAlternate("Geeks"))  # Output: "Ges"
print(sol.delAlternate("GeeksforGeeks"))  # Output: "GesoGes"

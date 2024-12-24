''' 
Given a string S as input. Delete the characters at odd indices of the string.
Input: S = "Geeks"
Output: "Ges" '''

class Solution:
    def delAlternate(self, S):
        return S[::2]

sol = Solution()
print(sol.delAlternate("Geeks"))  # Output: "Ges"
print(sol.delAlternate("GeeksforGeeks"))  # Output: "GesoGes"

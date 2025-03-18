'''
Remove all characters except the numeric characters from an alphanumeric string.

Input: S = "AA1d23cBB4"
Output: 1234'''

class Solution:
    def removeCharacters(self, S):
        result = ""
        
        for char in S:
            if char.isdigit():
                result += char
        
        return result

sol = Solution()
S1 = "AA1d23cBB4"
S2 = "a1b2c3"
print(sol.removeCharacters(S1))  # Output: "1234"
print(sol.removeCharacters(S2))  # Output: "123"

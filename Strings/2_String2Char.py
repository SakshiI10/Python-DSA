'''
Convert string to character.'''

class Solution:
    def strtochar(self, s):
        return list(s)

sol = Solution()
str = "qwerty"
result = sol.strtochar(str)
print("Characters in the string:", ' '.join(result))

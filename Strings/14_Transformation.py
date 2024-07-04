'''
Given a string S, consisting only of english alphabets, replace all the alphabets with the alphabets occuring at the same position when counted in reverse order of alphabets. For example, 'a' would be replaced by 'z', 'b' by 'y', 'c' by 'x' and so on. Any capital letters would be replaced by capital letters only.

Input: S = "Hello"
Output: Svool'''

class Solution:
    def convert(self, S):
        result = []
        
        for char in S:
            if char.isalpha():
                if char.islower():
                    new_char = chr(ord('z') - (ord(char) - ord('a')))
                else:
                    new_char = chr(ord('Z') - (ord(char) - ord('A')))
            else:
                new_char = char
            
            result.append(new_char)
        return ''.join(result)

S = "Hello"
sol = Solution()
output = sol.convert(S)
print(output)  # Output: Svool

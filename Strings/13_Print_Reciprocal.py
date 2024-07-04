''' 
Given a string S, we need to find reciprocal of it. The reciprocal of the letter is found by finding the difference between the position of the letter and the first letter ‘A’. Then decreasing the same number of steps from the last letter ‘Z’. The character that we reach after above steps is reciprocal.
Reciprocal of Z is A and vice versa because if you reverse the position of the alphabet A will be in the position of Z.
Similarly, if the letter is a small case then the first letter will be 'a' and the last letter will be 'z'. and the definition of reciprocal remains the same.

S = "ab C"
Output:
zy X
Explanation:
The reciprocal of the first letter 'a' is 'z'.
The reciprocal of the second letter 'b' is 'y'.
The reciprocal of the third letter ' ' is ' '.
The reciprocal of the last letter 'C' is 'X'.'''

class Solution:
    def reciprocalString(self, S):
        result = []
        for char in S:
            if 'A' <= char <= 'Z':
                reciprocal_char = chr(ord('Z') - (ord(char) - ord('A')))
                result.append(reciprocal_char)
            elif 'a' <= char <= 'z':
                reciprocal_char = chr(ord('z') - (ord(char) - ord('a')))
                result.append(reciprocal_char)
            else:
                result.append(char)
        return ''.join(result)

sol = Solution()
print(sol.reciprocalString("ab C"))  # Output: "zy X"
print(sol.reciprocalString("Ish"))   # Output: "Rhs"

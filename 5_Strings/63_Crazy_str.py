'''
You have given a non-empty string. This string can consist of lowercase and uppercase english alphabets. Convert the string into an alternating sequence of lowercase and uppercase characters without changing the character at the 0th index.

Example 1:

Input:
S = "geeksforgeeks"
Output: gEeKsFoRgEeKs'''

class Solution:
    def getCrazy(self, S):
        res = ""

        for i in range(len(S)):
            if i % 2 == 0:
                if S[0].islower():
                    res += S[i].lower()
                else:
                    res += S[i].upper()
            else:
                if S[0].islower():
                    res += S[i].upper()
                else:
                    res += S[i].lower()

        return res
    
sol=Solution()
S = "geeksforgeeks"
print(sol.getCrazy(S))
'''
Given a string S, check whether it can be converted into the string "hello" by deleting some characters from it.
Note : S can have both uppercase and lowercase letters.

Input:
S = "bbbbbxxhhelllllooudd"
Output: 1'''

class Solution:
    def decode(self, S):
        target='hello'
        j=0
        
        for char in S:
            if char == target[j]:
                j += 1
                if j==len(target):
                    return True
        return False

sol=Solution()
S = "bbbbbxxhhelllllooudd"
print(sol.decode(S))  

'''
Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.

Input:
S1 = "Hello" S2 = "Bye"
Output: HBeylelo
'''

class Solution:
    def merge(self, S1, S2):
        res=""
        i=0
        len1=len(S1)
        len2=len(S2)
        
        while i<len1 or i<len2:
            if i < len1:
                res += S1[i]
            if i < len2:
                res += S2[i]
            i += 1
            
        return res
    
sol= Solution()
S1 = "Hello"
S2 = "Bye"
print(sol.merge(S1, S2))  
'''
Given three strings S, oldW and newW. Find all occurrences of the word oldW in S and replace them with word newW.

Input: 
S = "xxforxx xx for xx"
oldW = "xx"
newW = "Geeks"
Output: 
"geeksforgeeks geeks for geeks" '''

class Solution:
    def replaceAll (self, S, oldW, newW):
        res = ""
        i = 0
        
        while i < len(S):
            if S[i:i+len(oldW)] == oldW:
                res += newW
                i += len(oldW)
            else:
                res += S[i]
                i += 1
        return res

sol=Solution()
S = "xxforxx xx for xx"
oldW = "xx"
newW = "Geeks"
print(sol.replaceAll(S, oldW, newW))

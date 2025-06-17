'''
Find the first occurrence of the string pat in the string txt. The function returns an integer denoting the first occurrence of the string pat in txt (0-based indexing).

Input: txt = "GeeksForGeeks", pat = "Fr"
Output: -1'''

class Solution:
    def firstOccurence(self,txt,pat):
        n=len(txt)
        m=len(pat)
        
        for i in range(n-m+1):
            match = True
            for j in range(m):
                if txt[i+j] != pat[j]:
                    match=False
                    break
            if match:
                return i
        return -1
    
sol= Solution()
txt = "GeeksForGeeks"
pat = "For"
print(sol.firstOccurence(txt, pat))  
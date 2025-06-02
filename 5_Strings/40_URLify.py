'''
Given a string s, replace all the spaces in the string with '%20'.

Input: s = "Mr Benedict Cumberbatch"i love programming
Output: "Mr%20Benedict%20Cumberbatch"'''

class Solution:
    def URLify(self, s): 
        res=""
        for char in s:
            if char != " ":
                res += char
            else:
                res += "%20"
                
        return res
    
sol=Solution()
print(sol.URLify("Mr Benedict Cumberbatch")) 
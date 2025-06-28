'''
You are given two strings s1 and s2. Your task is to identify the characters that appear in either string but not in both (i.e., characters that are unique to one of the strings). Return the result as a sorted string.

Input: s1 = "geeksforgeeks", s2 = "geeksquiz"
Output: "fioqruz"'''

class Solution:
    def uncommonChars(self, s1, s2):
        l1 = set(s1)
        l2 = set(s2)
        res = ''
        
        for char in l1:
            if char not in l2:
                res += char
                
        for char in l2:
            if char not in l1:
                res += char
                
        res = ''.join(sorted(res))
        return res
    
sol=Solution()
s1="geeksforgeeks"
s2="geeksquiz"
print(sol.uncommonChars(s1, s2))
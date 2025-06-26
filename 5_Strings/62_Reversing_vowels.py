'''
Given a string consisting of lowercase English alphabets, reverse only the vowels present in it and print the resulting string.

Input: s = "practice"
Output: "prectica"'''

class Solution:
    def modify(self, s):
        s=s.lower()
        vowels = set('aeiou')
        rev = ''
        
        for char in s:
            if char in vowels:
                rev += char
        
        rev = rev[::-1]
        
        res = ''
        count = 0
        for char in s:
            if char in vowels:
                res += rev[count]
                count += 1
            else:
                res += char
        
        return res
    
sol=Solution()
s='prActice'
print(sol.modify(s))
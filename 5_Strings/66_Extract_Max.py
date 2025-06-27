'''
Given a alphanumeric string S, extract maximum numeric value from S.

Input:
S = 100klh564abc365bg
Output: 564'''

class Solution:
    def extractMaximum(self,s): 
        res = []
        num = ''
        
        for char in s:
            if char.isdigit():
                num += char
            else:
                if num != '':
                    res.append(int(num))
                    num = ''
        
        if num != '':
            res.append(int(num))
        
        return max(res) if res else -1
    
sol=Solution()
S = '100klh564abc365bg'
print(sol.extractMaximum(S))
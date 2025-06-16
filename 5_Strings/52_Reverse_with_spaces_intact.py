'''
Given a string, your task is to reverse the string keeping the spaces intact to their positions.

Input:
S = "Help others"
Output: sreh topleH'''

class Solution:
    def reverseWithSpacesIntact(self, s):
        temp = ""
        for char in s:
            if char != ' ':
                temp += char
        temp = temp[::-1]
        
        res = ""
        index = 0
        for char in s:
            if char == ' ':
                res += ' '
            else:
                res += temp[index]
                index += 1
                
        return res
    
sol= Solution()
s = "Help others"
print(sol.reverseWithSpacesIntact(s))  
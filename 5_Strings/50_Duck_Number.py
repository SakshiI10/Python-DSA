'''
The task is to check whether the given number N is a Duck number or not.

Input: 707069
Output: YES
Explanation: 707069 contains a non-leading 0.
 
Input: 02364
Output: NO
Explanation: contains only leading 0.
'''

class Solution:
    def isDuckNumber(self, N):
        if N[0] == '0':
            return "NO"
        
        for char in N[1:]:
            if char == '0':
                return "YES"
        return "NO"
    
sol = Solution()
print(sol.isDuckNumber("707069"))  
print(sol.isDuckNumber("02364"))   

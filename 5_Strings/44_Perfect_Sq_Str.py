'''
You are given a string S. Your task is to determine if the sum of ASCII values of all character results in a perfect square or not. If it is a perfect square then the answer is 1, otherwise 0.

Input: S = "d"
Output: 1'''

class Solution:
    def isSquare(self, S): 
        total = sum(map(ord, S))
        root = int(total ** 0.5)
        
        if root * root == total:
            return 1
        else:
            return 0
        
sol= Solution()
print(sol.isSquare("d"))  
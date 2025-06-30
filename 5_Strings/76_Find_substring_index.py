'''
Given two strings X and Y, the task is to find the last index in X at which string Y appears, if Y does not appear then the answer is -1.

Input: X = "geeksforgeeks", Y = "geeks"
output: 9'''

class Solution:
    # Return both index
    def search1(self, X, Y):
        res = []
        for i in range(len(X) - len(Y) + 1):
            if X[i:i+len(Y)] == Y:
                res.append(i+1)
        return res if res else [-1]
    
    # Return last index
    def search2(self, X, Y):
        index = X.rfind(Y)
        
        if index != -1:
            return index + 1 
        else:
            return -1

sol=Solution()
X = "geeksforgeeks"
Y = "geeks"
print(sol.search1(X, Y))
print(sol.search2(X, Y))
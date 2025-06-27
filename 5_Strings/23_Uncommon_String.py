'''
Given two strings A and B consisting of lowercase english characters. Find the characters that are not common in the two strings. 

Input:
A = geeksforgeeks
B = geeksquiz
Output: fioqruz'''

class Solution:
    def UncommonChars(self, A, B):
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

solution = Solution()
A = "geeksforgeeks"
B = "geeksquiz"
output = solution.UncommonChars(A, B)
print(output)  # Expected output: fioqruz

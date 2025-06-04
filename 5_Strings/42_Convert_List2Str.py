'''
Convert a list of characters into a String
Difficulty: BasicAccuracy: 63.69%Submissions: 30K+Points: 1
Given a list of characters, merge all of them into a string.

Input:
N = 13
Char array = g e e k s f o r g e e k s
Output: geeksforgeeks '''

class Solution:
    def chartostr(self, arr,N):
        res = ""
        for char in arr:
            if char != " ":
                res += char
        return res
    
sol = Solution()
N = 13
arr = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(sol.chartostr(arr, N))  
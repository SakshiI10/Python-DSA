'''Geek is at a book fair. There are total N kinds of books. He has to choose a book of a particular kind and read it loudly as many times as he can in the given time and earn points. Geek knows that reading a book of kind i once needs Ai minutes and it will give him Bi points. Geek has K minutes for reading books. During this time, he can only read a book of a particular kind as many times as he can so as to maximize his points. But he can not pick books of different kinds, he has to read the same book again and again. Find the maximum points Geek can get. 

Input: 
N = 3, K = 10
A = {3, 4, 5}
B = {4, 4, 5}
Output: 12'''

class Solution:
    def maxPoint(self, N, K, A, B):
        

sol = Solution()
print(sol.maxPoint(3, 10, [3, 4, 5], [4, 4, 5])) 

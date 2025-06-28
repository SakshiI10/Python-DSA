'''
Bingu was testing all the strings he had at his place and found that most of them were prone to a vicious attack by Banju, his arch-enemy. Bingu decided to encrypt all the strings he had, by the following method. Every substring of identical letters is replaced by a single instance of that letter followed by the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it.

Input:
s = "aabc"
Output: 1c1b2a'''

class Solution:

    def encryptString(self, s):
        n = len(s)
        res = ''
        count = 1

        for i in range(1, n + 1):
            if i < n and s[i] == s[i - 1]:
                count += 1
            else:
                res += s[i - 1] + str(count)
                count = 1
                 
        return res[::-1]
    
sol=Solution()
s="aabc"
print(sol.encryptString(s))

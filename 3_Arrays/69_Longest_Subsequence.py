from typing import List

class Solution():
    #Brute Force
    def getLongestSubarray(self, a, k):
        n=len(a)
        length=0

        for i in range(n):
            s=0
            for j in range(i+1, n):
                s += a[j]

                if s==k:
                    return max(length, j-i+1)
        return length

sol=Solution()
a = [2, 3, 5, 1, 9]
k = 10
len1 = sol.getLongestSubarray(a, k)
print(len1)

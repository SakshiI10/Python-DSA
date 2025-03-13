from typing import List

class Solution():
    #Brute Force
    def getLongestSubarray(self, a: [int], k: int) -> int:
        n = len(a)
        length = 0
        
        for i in range(n): # starting index
            s = 0
            for j in range(i, n): # ending index
                # add the current element to the subarray a[i...j-1]:
                s += a[j]

                if s == k:
                    length = max(length, j - i + 1)
        return length

sol=Solution()
a = [2, 3, 5, 1, 9]
k = 10
len1 = sol.getLongestSubarray(a, k)
print(len1)

from typing import List

class Solution:
    # Brute Force
    def foursum(self, arr: List[int], target: int):
        n = len(arr)
        arr.sort()
        res=[]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):  
                    for l in range(k+1, n):
                        if arr[i] + arr[j] + arr[k] + arr[l]== target:
                            quadret=[arr[i], arr[j], arr[k], arr[l]]
                            if quadret not in res:
                                res.append(quadret)
        return res

sol = Solution()
a = [1, 0, -1, 0, -2, 2]
k = 0
len1 = sol.foursum(a, k)
print(len1)

# Better solution is done using hashing
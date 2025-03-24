from typing import List

class Solution:
    # Brute Force
    def threesum(self, arr: List[int], target: int):
        n = len(arr)
        arr.sort()
        res=[]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):  
                    if arr[i] + arr[j] + arr[k] == target:
                        triplet=[arr[i], arr[j], arr[k]]
                        if triplet not in res:
                            res.append(triplet)
        return res

sol = Solution()
a = [-1, 0, 1, 2, -1, -4]
k = 0
len1 = sol.threesum(a, k)
print(len1)

# Better solution is done using hashing
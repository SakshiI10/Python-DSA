from typing import List

class Solution():
    def foursum(self, arr: List[int], target: int):
        # arr.sort()
        n=len(arr)
        res = set()

        for i in range(n):
            hash_table = set()  
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    complement = target - (arr[i] + arr[j] + arr[k])
                    if complement in hash_table:
                        quadret = (arr[i], arr[j], arr[k], complement)
                        res.add(tuple(sorted(quadret)))  
                    hash_table.add(arr[k])

        return [list(quadret) for quadret in res] if res else "No"
                
sol=Solution()
a = [1, 0, -1, 0, -2, 2]
k = 0
len1 = sol.foursum(a, k)
print(len1)

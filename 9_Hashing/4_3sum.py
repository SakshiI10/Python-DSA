from typing import List

class Solution():
    def threesum(self, arr: List[int], target: int):
        n = len(arr)
        hash_table = set()        
        res = set()          

        for i in range(n):
            for j in range(i + 1, n):
                complement = target - (arr[i] + arr[j])
                if complement in hash_table:
                    triplet = (arr[i], arr[j], complement)
                    res.add(tuple(sorted(triplet)))
            hash_table.add(arr[i]) 

        return [list(triplet) for triplet in res] if res else "No"
                
sol=Solution()
a = [-1, 0, 1, 2, -1, -4]
k = 0
len1 = sol.threesum(a, k)
print(len1)

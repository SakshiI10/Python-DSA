from typing import List

class Solution():
    def twosum(self, arr: List[int], k: int):
        hash_table={}
        n=len(arr)

        for i in range(n):
            compliment=k-arr[i]
            if compliment in hash_table:
                print("Yes")
                return [hash_table[compliment], i]
            hash_table[arr[i]] = i
                

sol=Solution()
a = [2, 6, 5, 8, 11]
k = 10
len1 = sol.twosum(a, k)
print(len1)

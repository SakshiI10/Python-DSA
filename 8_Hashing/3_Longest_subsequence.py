from typing import List

class Solution:
    def longest_sub_hashing(self, a: List[int], k: int) -> int:
        hash_table = {}  # Dictionary to store (prefix_sum, index)
        n = len(a)
        sum = 0
        length = 0

        for i in range(n):
            sum += a[i]

            if sum == k:
                length = max(length, i + 1)

            rem = sum - k

            if rem in hash_table:
                length = max(length, i - hash_table[rem])

            if sum not in hash_table:
                hash_table[sum] = i  

        return length 

sol = Solution()
a = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
k = 3
len1 = sol.longest_sub_hashing(a, k)
print(len1)

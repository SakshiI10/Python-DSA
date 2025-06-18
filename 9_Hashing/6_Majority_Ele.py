class Solution:
    def majority(self, arr):
        hash_table={}
        n=len(arr)

        for num in arr:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num]=1
        for key, value in hash_table.items():
            if value > n//2:
                return key
        return -1
            
sol=Solution()
arr=[2, 2, 3, 3, 1, 2, 2]
print(sol.majority(arr))

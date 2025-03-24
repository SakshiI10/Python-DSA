class Solution:
    def majority(self, arr):
        hash_table={}
        n=len(arr)
        res=[]
        for num in arr:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num]=1
        for key, value in hash_table.items():
            if value > n//3:
                res.append(key)
        return res if res else -1
            
sol=Solution()
arr=[1, 1, 1, 3, 3, 2, 2, 2]
print(sol.majority(arr))

class Solution:
    def max_subarray(self, arr, k):
        count=0
        prefix_sum=0
        hash_map={0: 1}

        for num in arr:
            prefix_sum += num
            if prefix_sum-k in hash_map
        
    
sol=Solution()
arr=[1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k=3
print(sol.max_subarray(arr, k))

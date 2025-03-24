class Solution:
    def max_subarray(self, arr, k):
        count=0
        prefix_sum=0
        hash_map={0: 1}

        for num in arr:
            prefix_sum += num
            if prefix_sum-k in hash_map:
                # # Add occurrences of (prefix_sum - k)
                count += hash_map[prefix_sum-k]
            # Store/update the count of this prefix sum
            hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
        return count
    
sol=Solution()
arr=[1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k=3
print(sol.max_subarray(arr, k))

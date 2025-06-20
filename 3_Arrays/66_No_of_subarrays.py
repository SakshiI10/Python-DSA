class Solution:
    #Brute Force
    def max_subarray(self, arr, k):
        n=len(arr)
        count=0
        for i in range(n):
            sum=0
            for j in range(i, n):
                sum += arr[j]
                if sum == k:
                    count += 1
        return count
    
sol=Solution()
arr=[1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k=3
print(sol.max_subarray(arr, k))

# Better solution is done using hashing
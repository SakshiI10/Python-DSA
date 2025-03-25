class Solution:
    def majority(self, arr):
        #Brute Force
        n=len(arr)
        for i in range(n):
            count=0
            for j in range(n):
                if (arr[i]==arr[j]):
                    count += 1
        if count>n//2:
            return arr[i]
        return -1
            
sol=Solution()
arr=[2, 2, 3, 3, 1, 2, 2]
print(sol.majority(arr))

# Better solution is done using hashing
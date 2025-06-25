# This will return count as well as the numbers.

class Solution:
    #Brute Force
    def max_subarray(self, arr, k):
        n=len(arr)
        count=0
        res=[]

        for i in range(n):
            sum=0
            temp=[]
            for j in range(i, n):
                sum += arr[j]
                temp.append(arr[j])

                if sum == k:
                    count += 1
                    res.append(temp[:])
        return count, res
    
sol=Solution()
arr=[1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k=3
print(sol.max_subarray(arr, k))

# Better solution is done using hashing
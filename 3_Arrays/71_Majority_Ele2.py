class Solution:
    def majority(self, arr):
        #Brute Force
        n=len(arr)
        ans=[]
        for i in range(n):
            count=0
            for j in range(n):
                if (arr[i]==arr[j]):
                    count += 1
            if count>n//3 and arr[i] not in ans:
                ans.append(arr[i])
        return ans if ans else -1
            
sol=Solution()
arr=[1, 1, 1, 3, 3, 2, 2, 2]
print(sol.majority(arr))

#Not efficient, so did it using dictionary (present in hashing folder)
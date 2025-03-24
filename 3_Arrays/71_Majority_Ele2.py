class Solution:
    def majority(self, arr):
        #Brute Force
        n=len(arr)
        res=[]
        for i in range(n):
            count=0
            for j in range(n):
                if (arr[i]==arr[j]):
                    count += 1
            if count>n//3 and arr[i] not in res:
                res.append(arr[i])
        return res if res else -1
            
sol=Solution()
arr=[1, 1, 1, 3, 3, 2, 2, 2]
print(sol.majority(arr))

#Not efficient, so did it using dictionary (present in hashing folder)
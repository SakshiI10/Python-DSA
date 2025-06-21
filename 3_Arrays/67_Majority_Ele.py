'''
You are given an array arr, and your task is to find the majority element an element that occurs more than half the length of the array (i.e., arr.size() / 2). If such an element exists return it, otherwise return -1, indicating that no majority element is present.

Input : arr[] = [1, 1, 2, 1, 3, 5, 1]
Output : 1'''

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

            if count>n//2 and arr[i] not in res:
                res.append(arr[i])
        return res if res else -1
            
sol=Solution()
arr=[2, 2, 3, 3, 1, 2, 2]
print(sol.majority(arr))

# Better solution is done using hashing
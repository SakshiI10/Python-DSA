from typing import List

class Solution():
    #Brute Force - index
    def twosum(self, arr: List[int], k: int):
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                if (arr[i]+arr[j] == k):
                    print("Yes")
                    return i, j 
        print("No")       
        return -1,-1
    
    # Brute Force - Values
    def twosum2(self, arr, k):
        n=len(arr)
        res=[]

        for i in range(n):
            for j in range(i+1, n):
                if (arr[i] + arr[j] == k):
                    double=[arr[i], arr[j]]
                    if double not in res:
                        res.append(double)
        return res

sol=Solution()
a = [2, 6, 5, 8, 11]
k = 14
len1 = sol.twosum(a, k)
len1 = sol.twosum2(a, k)
print(len1)

# Better solution is done using hashing
from typing import List

class Solution():
    #Brute Force
    def twosum(self, arr: List[int], k: int):
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                if (arr[i]+arr[j] == k):
                    print("Yes")
                    return i, j 
        print("No")       
        return -1,-1

sol=Solution()
a = [2, 6, 5, 8, 11]
k = 14
len1 = sol.twosum(a, k)
print(len1)

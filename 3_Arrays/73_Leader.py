class Solution:
    def leader(self, arr, n):
        result = []
        for i in range(n):
            leader = True
            for j in range(i + 1, n):
                if arr[j] > arr[i]:  
                    leader = False
                    break
            if leader==True:  
                result.append(arr[i])
        return result

sol = Solution()
arr1 = [10, 22, 12, 3, 0, 6]
print(sol.leader(arr1, len(arr1)))  # Print the result instead of arr1

class Solution:
    def longest_cons_subseq(self, arr, n):
        for i in range(n):
            num = arr[i]
            count=0
            while num+1 in arr:
                count += 1
                num += 1
        return count

sol = Solution()
arr1 = [102, 4, 100, 1, 101, 3, 2, 1, 1]
print(sol.longest_cons_subseq(arr1, len(arr1)))  
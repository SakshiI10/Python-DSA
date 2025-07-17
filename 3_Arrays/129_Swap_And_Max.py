'''Given an array arr[ ] of positive elements. Consider the array as a circular array, meaning the element after the last element is the first element of the array. The task is to find the maximum sum of the absolute differences between consecutive elements with shuffling of array elements allowed i.e. shuffle the array elements and make [a1..an] such order that  |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1| is maximized.

Input: arr[] = [4, 2, 1, 8]
Output: 18'''

class Solution:
    def maxSum(self,arr):
        res = []
        arr.sort()
        n = len(arr)

        start, end = 0, n - 1
        while start < end:
            res.append(arr[start])
            res.append(arr[end])
            start += 1
            end -= 1

        if start == end:
            res.append(arr[start])  

        total = 0
        for i in range(n):
            total += abs(res[i] - res[(i + 1) % n])  
            
        return total

sol=Solution()
arr = [4, 2, 1, 8]
print(sol.maxSum(arr))

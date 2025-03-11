from typing import List

class Solution():
    #Brute Force
    def getLongestSubarray(self, a: [int], k: int) -> int:
        n = len(a)
        length = 0
        
        for i in range(n): # starting index
            s = 0
            for j in range(i, n): # ending index
                # add the current element to the subarray a[i...j-1]:
                s += a[j]

                if s == k:
                    length = max(length, j - i + 1)
        return length

    #Two pointer
    def getLongestSubarray2(self, a: [int], k: int) -> int:
        n = len(a) # size of the array.

        left, right = 0, 0 # 2 pointers
        Sum = a[0]
        maxLen = 0
        while right < n:
            # if sum > k, reduce the subarray from left
            # until sum becomes less or equal to k:
            while left <= right and Sum > k:
                Sum -= a[left]
                left += 1

            # if sum = k, update the maxLen i.e. answer:
            if Sum == k:
                maxLen = max(maxLen, right - left + 1)

            # Move forward the right pointer:
            right += 1
            if right < n: Sum += a[right]

        return maxLen

sol=Solution()
a = [2, 3, 5, 1, 9]
k = 10
len1 = sol.getLongestSubarray(a, k)
len2 = sol.getLongestSubarray2(a, k)
print("The length of the longest subarray is:", len1)
print(f"The length of the longest subarray is: {len2}")

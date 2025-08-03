'''
Given an array, the task is to find the difference between the highest occurrence and lowest occurrence of any number in an array.
Note: If only one type of element is present in the array return 0.

Input: arr[] = [1, 2, 2]
Output: 1'''

class Solution:
    def findDiff(self, arr):
        freq={}
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
                
        counts = list(freq.values())
        
        highest = max(counts)
        lowest = min(counts)
        
        return abs(highest - lowest)
    
sol=Solution()
arr=[1, 2, 2]
print(sol.findDiff(arr))

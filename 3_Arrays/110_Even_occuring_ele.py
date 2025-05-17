'''
Given an array arr[] of integers, where most numbers occur an odd number of times, except for a few elements that appear an even number of times. Find and return the elements with even occurrences in the array.
If no such element exists, return -1.

Input: arr[] = [9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
Output: [12, 15, 23]
'''

class Solution:
    def findEvenOccurrences(self, arr):
        freq={}
        res=[]
        
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
                
        for num, count in freq.items():
            if count%2==0:
                res.append(num)  
                
        return res if res else [-1]
    
sol=Solution()
arr=[9, 12, 23, 10, 12, 12, 15, 23, 14, 12, 15]
print(sol.findEvenOccurrences(arr))
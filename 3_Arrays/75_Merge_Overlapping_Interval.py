class Solution:
    def merge_int(self, arr):
        arr.sort()
        res=[]

        # If res is empty or the current interval does not overlap, add it to res.
        # If it overlaps, merge it by updating the last interval in res.
        for interval in arr:
            # res[-1] → Last interval in res
            # res[-1][0] → Start of the last interval
            # res[-1][1] → End of the last interval
            # interval[1] → End of the current interval
            if not res or interval[0]>res[-1][1]:
                res.append(interval)
            else:
                res[-1]=(res[-1][0], max(res[-1][1], interval[1]))
        return res

sol=Solution()
arr=[(1, 3), (2, 4), (2, 6), (8, 9), (8, 10), (9, 11), (15, 18), (16, 17)]
merged_intervals = sol.merge_int(arr)
print(merged_intervals)
'''
Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true'''

from collections import Counter

def is_subset(a, b):
    for i in range(len(b)):
        if b[i] not in a:
            return 'false'
    return 'true'

    # count_a = Counter(a)
    # count_b = Counter(b)

    # for i in count_b:
    #     if count_b[i] > count_a.get(i, 0):
    #         return False
    # return True
    
a = [10, 5, 2, 23, 19]
b = [19, 5, 3]
print(is_subset(a, b))  # Output: True
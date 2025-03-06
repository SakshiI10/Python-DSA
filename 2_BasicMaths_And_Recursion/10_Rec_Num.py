# Print number from 1 to N using Recursion.

def rec(i, n):
    if i>n:
        return
    print(i)
    rec(i+1, n)

n=5
i=1
rec(i, n)

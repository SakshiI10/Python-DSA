# Print number from 1 to N using Recursion.
def rec(i, n):
    if i>n:
        return
    print(i)
    rec(i+1, n)

n=5
i=1
rec(i, n)

print()

# Print number from N to 1 using Recursion.
def rec(i, n):
    if i<1:
        return
    print(i)
    rec(i-1, n)

n=5
i=5
rec(i, n)

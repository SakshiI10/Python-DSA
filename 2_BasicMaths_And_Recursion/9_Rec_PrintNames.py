# Print your name 5 times using Recursion.

def rec(n):
    if n==0:
        return
    print("Sakshi")
    rec(n-1)

n=5
rec(n)
'''
**********
****  ****
***    ***
**      **
*        *
**      **
***    ***
****  ****
**********'''

def print_pattern(n):
    for i in range(n):
        for j in range(1, n-i+1):
            print("*", end="")

        for j in range(2*i):
            print(" ", end="")

        for j in range(n-i):
            print("*", end="")

        print()

    for i in range(1, n):
        for j in range(i+1):
            print("*", end="")

        for j in range(1, 2*(n-i)-1):
            print(" ", end="")

        for j in range(i+1):
            print("*", end="")

        print()

n=5
print_pattern(n)
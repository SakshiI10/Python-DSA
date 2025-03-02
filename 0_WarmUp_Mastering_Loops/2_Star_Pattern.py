'''
*
**
***
****
***** '''

def pattern_using_one_loop(n):
    for i in range(n+1):
        print("*"*i)

def pattern_using_two_loops(n):
    for i in range(n+1):
        for j in range(i):
            print('*', end="")
        print()

n=5
pattern_using_one_loop(n)
pattern_using_two_loops(n)

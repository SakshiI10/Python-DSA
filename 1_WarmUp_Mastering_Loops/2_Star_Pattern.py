'''
*
**
***
****
***** '''

def pattern_using_single_loop(n):
    for i in range(1, n+1):
        print("*"*i)

def pattern_using_nested_loops(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end="")
        print()

n=5
pattern_using_single_loop(n)
print()
pattern_using_nested_loops(n)

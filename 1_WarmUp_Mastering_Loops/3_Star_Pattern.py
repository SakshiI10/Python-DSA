'''
*****
****
***
**
* '''

def pattern_using_single_loop(n):
    for i in range(n, 0, -1):
        print('*' * i)

def pattern_using_nested_loop(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

n=5
pattern_using_single_loop(n)
pattern_using_nested_loop(n)

'''
*****
 ****
  ***
   **
    * '''

def pattern_using_single_loop(n):
    for i in range(n):
        print(' '*i + '*'*(n-i))

def pattern_using_nested_loops(n):
    for i in range(n):
        for j in range(i):
            print(' ', end='')
        for j in range(n-i):
            print('*', end='')
        print()

n=5
pattern_using_single_loop(n)
pattern_using_nested_loops(n)

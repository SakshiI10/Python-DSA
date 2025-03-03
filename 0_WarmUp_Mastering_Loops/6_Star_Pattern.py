'''
    *
   ***
  *****
 *******
********* '''

def pattern_using_single_loop(n):
    for i in range(n):
        print(' '*(n-i-1)+'*'*(2*i+1))

def pattern_using_nested_loops(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='') 
        for j in range(2*i + 1):
            print('*', end='')  
        print()


n=5
pattern_using_single_loop(n)
pattern_using_nested_loops(n)

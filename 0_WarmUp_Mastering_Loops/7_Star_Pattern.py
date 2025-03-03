'''
*********
 *******
  *****
   ***
    * '''

def pattern_using_single_loop(n):
    for i in range(n):
        print(' '*i + '*'*(2*(n-i)-1))

def pattern_using_nested_loops(n):
    for i in range(n):
        for j in range(i):
            print(' ', end='') 
        for j in range(2*(n-i)-1):
            print('*', end='')  
        print()

n=5
pattern_using_single_loop(n)
pattern_using_nested_loops(n)

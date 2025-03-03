'''
*****
 ****
  ***
   **
    * '''

def pattern_using_single_loop(n):
    for i in range(n):
        print(' '*i + '*'*(n-i))

n=5
pattern_using_single_loop(n)

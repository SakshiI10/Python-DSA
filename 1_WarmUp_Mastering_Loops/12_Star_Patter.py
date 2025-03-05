'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    * '''

def print_patterns(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        print()

    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print()

n=5
print_patterns(n)

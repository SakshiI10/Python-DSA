'''
   A
  ABA
 ABCBA
ABCDCBA'''

def print_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")

        char=65
        for j in range(2*i+1):
            breakpoint=(2*i+1)//2
            print(chr(char), end="")
            if j < breakpoint:
                char += 1
            else:
                char -= 1

        print()

n=4
print_pattern(n)

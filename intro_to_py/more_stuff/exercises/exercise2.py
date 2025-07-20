# Use sqrt function from math library to write some code that
# outputs the square root of 37.  Try to write the code in three
# different ways

# import math
# import math as m    Two other forms

from math import sqrt

#1
print(sqrt(37))

#2
def square_root(number):
    num = sqrt(number)
    return num

print(square_root(37))


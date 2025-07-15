def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

"""
multiply is a function name                                    -line 1,9
left is a parameter                                            -line 1,2
right is a parameter                                           -line 1,2
get_num is a function name                                     -line 4,7,8
prompt is a parameter                                          -line4,5
float is a function name                                       -line 5
input is a function name                                       -line 5
print is a function name                                       -line 10
"""
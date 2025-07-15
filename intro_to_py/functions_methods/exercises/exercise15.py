def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


"""
multiply is global
left is local
right is local
get_num is global
prompt is local
float is built in
input is built in
first_number is global
second_number is global
product is global
print is built in
"""
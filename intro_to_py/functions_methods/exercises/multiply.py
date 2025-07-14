print()
print('This program multiplies two numbers and gives the result.\n')
#number1 = float(input('Please enter your first number '))
#number2 = float(input('Please enter your second number '))
def get_num(prompt):
    entry = input(prompt)
    return float(entry)

number1 = get_num('Please enter your first number ')
number2 = get_num('please enter your second number ')

def multiply(num1, num2):
    return num1 * num2

result = multiply(number1,number2)
print(f'{number1:,} multiplied by {number2:,} equals {result:,}\n\n')





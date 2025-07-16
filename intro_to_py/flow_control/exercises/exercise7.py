"""
Write a function that takes a single integer argument and prints a 
message that describes whether: 1 the value is between 0 and 50
2 the value is between 51 and 100 (inclusive) 3 the value is greater than 100
4 the value is less than 0
"""
def number_range(num):
    if (num >= 0) and (num <= 50):
        print(f'{num} is in the range of 0 to 50')
    elif (num >= 51) and (num <= 100):
        print(f'{num} is in the range of 51 to 100')
    elif num > 100:
        print(f'{num} is greater than 100')
    else:
        print(f'{num} is less than 0')

digit = int(input('\nenter a number\n'))
number_range(digit)

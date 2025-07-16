def even_or_odd(number):
    if number % 2 == 0:
        print(f'{number} is an even number')
    else:
        print(f'{number} is an odd number')

print('\n\n')
print('This is a program that will tell you if the number you enter is even or odd\n')
digit = int(input('Enter the number you wish to test '))

even_or_odd(digit)

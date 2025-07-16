value1 = int(input('Please enter a number between 0 and 10:  '))

match value1:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 or 6')

value2 = int(input('Enter a second number between 0 and 10:  ' ))
             
match value2:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _: # default case
        print('value is not 1, 2, 3, or 4')
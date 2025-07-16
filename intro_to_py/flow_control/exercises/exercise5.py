def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# This code outputs the string 'Empty' because the
# argument given to is_list_empty is falsey and so does
# not trigger the if statement and runs the else statement instead
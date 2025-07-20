# Write code that creates a new list with one element for each number
# in my_list. If the original number is even, then the corresponding 
# element in the new list should contain 'even; otherwise 'odd'. 

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
for number in my_list:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

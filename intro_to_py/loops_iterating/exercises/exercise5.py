# Print all of the even numbers in the following list of nested litst.
# Don't use any while loops

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
for array in my_list:
    for number in array:
        if number % 2 == 0:
            print(number)

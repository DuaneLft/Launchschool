# Print all of the even numbers in the following list of nested lists.
# don't use for loops

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]
counter1 = 0

while counter1 < len(my_list):
    counter2 = 0
    while counter2 < len(my_list[counter1]):
        if my_list[counter1][counter2] % 2 == 0:
            print(my_list[counter1][counter2])
        counter2 += 1
    counter1 += 1
    
        
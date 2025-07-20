# Use a while loop to print all numbers in my_list with even values
# one number per line. Then print the odd numbers using a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

counter = 0
while counter < len(my_list):
    if my_list[counter] % 2 == 0:
        print(my_list[counter])
    counter += 1

print()

for number in my_list:
    if number % 2 != 0:
        print(number)


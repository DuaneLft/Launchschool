# Use a while loop to print the numbers in my_list. one number per lin
# Then do the same with a for loop

my_list =[6, 3, 0, 11, 20, 4, 17]
counter = 0
while counter < len(my_list):
    print(my_list[counter])
    counter += 1

for number in my_list:
    print(number)


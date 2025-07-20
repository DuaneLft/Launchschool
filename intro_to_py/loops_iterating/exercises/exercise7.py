# Write a find_integer function that returns a list of all the 
# integers from my_tuple
# [ expression for element in collection if expression ]
# [element for element in array if type(element == int)]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)


def find_integer(array):
    my_list = []
    for element in array:
        if type(element) == int:
            my_list.append(element)
    return my_list
            

new_list = find_integer(my_tuple)
print(new_list)
#----------------------------------------------------------------
# Below is the same with list comprehension
def find_int(array):
    return [element for element in array if type(element) == int]

new_list2 = find_int(my_tuple)
print(new_list2)
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

#Given the above code, answer the following questions and explain
#your answers:

"""
1. Are the lists assigned to my_list and another_list equal?
    Yes because they have the same values.    


2. Are the lists assigned to my_list and another_list the same object?
    No, even though their values are the same they are two different objects

3. Are the nested lists at index 3 of my_list and another_list equal?
    Yes they are equal because they have the same value


4.Are the nested lists at index 3 of my_list and another_list the same object?
    Yes they are because the list constructor performs a shallow copy
"""
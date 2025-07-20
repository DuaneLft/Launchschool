dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# What will this print and why

# I think since it is a nested element the change will be reflected in dict2 and print [1, 42, 3]
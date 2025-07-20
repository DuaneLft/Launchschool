my_dict = {'a': 1, 'b': 2, 'c': 3}# Looping over dictionary keys
for key in my_dict:
    print(key)

for values in my_dict.values():# Looping over dictionary values
    print(values)

for item in my_dict.items():#Looping over dictionary key/value pairs
    print(item)

# A more Pythonic way to iterate over both the keys and values
# simultaneously is to use tuple unpacking:

for key, value in my_dict.items():
    print(f'{key} = {value}')
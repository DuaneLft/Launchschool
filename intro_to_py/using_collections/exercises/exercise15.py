pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# Without running the following code what value will be printed by line 10?

# It will print 'Cat', 'Dog', 'Bird'. Because the keys variable was set before the changes the the pets
# dictionary was made

# I was wrong, I didn't know that the changes would be reflected in the keys variable
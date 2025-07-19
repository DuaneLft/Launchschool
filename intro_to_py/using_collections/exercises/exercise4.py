pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

"""
given the above dictionary:
1.Write some code to print Bark by accessing the element 
  associated with the key Dog.
2.Write some code to print None when you try to print the
  value associated with the non-existent key Lizard.
3.Write some code to print <silence> when you try to
  print the value associated with the non-existent key, Lizard  
"""
#1.
print(pets['Dog'])
#2
print(pets.get('Lizard'))
#3
print(pets.get('Lizard', '<silence>'))

# Without running code, what will it print and why

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# I'm guessing that since the range function adds a nested element to the set that both variables will refrence the same addition

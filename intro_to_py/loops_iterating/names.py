names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
"""
index = 0

while index < len(names):
    #upper_name = names[index].upper()
    upper_names.append(names[index].upper())
    index += 1

print(upper_names)"""

for name in names:
    if name == 'Max':# Could replace this and below with, if name != 'Max':
        continue
    upper_name = name.upper()
    upper_names.append(upper_name)
print(upper_names)


    
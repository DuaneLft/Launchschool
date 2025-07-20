# modified age.py using for loop
print()
age = int(input('Please Enter your age '))
print(f'You are {age} years old\n')
multiple = range(10,41,10)
for number in range(10,41,10):
    print(f'In {number} years you will be {number + age} years old\n')



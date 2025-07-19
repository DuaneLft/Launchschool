numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

# Write some code that determines and prints where the numbrer 3 appears inside each of the above lists
def find_three(numbers):
    if (3 in numbers):
        print(f'The number 3 is at position {numbers.index(3)} in {numbers}\n')
    else:
        print("The number 3 is not in this list.\n")

find_three(numbers1)
find_three(numbers2)
find_three(numbers3)
find_three(numbers4)
find_three(numbers5)


def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers1 = [0, 1, 2, 3, 4, 5, 6]
numbers2 = [1, 2, 4, 5]
numbers3 = [0, 3, 6]
numbers4 = []

print(f'The list, {numbers1}, has element not divisible by 3: {any(remainders_3(numbers1))}')
print(f'The list, {numbers2}, has element not divisible by 3: {any(remainders_3(numbers2))}')
print(f'The list, {numbers3}, has element not divisible by 3: {any(remainders_3(numbers3))}')
print(f'The list, {numbers4}, has element not divisible by 3: {any(remainders_3(numbers4))}')
      
# Write a function that computes and returns the factorial of a
# number by using a for or while loop. 1558! is the largest that can be run

def factorial(number):
    sum = 1
    for num in range(1, number + 1):
        sum *= num
    return sum

result = factorial(1558)
print(result)
        
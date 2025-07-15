def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))


#which identifiers are function names method names built in functions
"""
say         - function name
print       - function name, built in function
input       - function name, built in function
max         - function name, built in function
upper       - method name, built in function
lower        -method name, built in function
"""
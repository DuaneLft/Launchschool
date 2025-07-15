def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

#I think there will be an error because the third parameter
# doesn't have a default value and it must because the parameter
# before it has one
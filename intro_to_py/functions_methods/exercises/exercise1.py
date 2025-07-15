def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# I think this will throw an error because the foo variable is local to the set_foo function and will not be read by print()
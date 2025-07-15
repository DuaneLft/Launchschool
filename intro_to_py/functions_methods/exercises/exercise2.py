foo = 'bar'
def set_foo():
    foo = 'qux'

set_foo()
print(foo)

#This should print the string 'bar' because it is the value for the foo in the
#print functions scope.
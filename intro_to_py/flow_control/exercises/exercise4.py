def baz():
    return ('bar' if foo() else qux()) 

# Below is the above with regular if statements

def baz():
    if foo():
        return 'bar'
    else:
        return qux()
def top():
    bottom()

def bottom():
    print('Reached the bottom')

top()
def foo():
    def bar():
        print('BAR')

    bar() # BAR

foo()
greeting = 'Salutations'

def well_howdy(who):
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)
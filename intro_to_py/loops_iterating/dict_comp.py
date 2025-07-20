from pprint import pprint as pp

squares = {f'{number}-squared': number * number for number in range(0,11)}
pp(squares)

set_squares = {number * number for number in range(10,101)}
pp(set_squares)

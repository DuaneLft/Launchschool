def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# line 12 prints 'Product2' because it is matched by case '113'
# line 13 prints 'Product not found!' because all the cases look for a string and 142 is not a string
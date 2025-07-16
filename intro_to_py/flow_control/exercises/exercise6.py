"""
Write a function that takes a string as an argument and returns
an all-caps version of the string when the string is longer than 10
characters. Otherwise, it should return the original string
"""

def format_long_string(text):
    if len(text) > 10:
        return text.upper()
    else:
        return text
    
message = input('\nPlease enter some text ')

print(f'\n{format_long_string(message)}\n')

        
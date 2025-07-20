counter = 0

while counter < 5:
    print(counter)

# This cause causes an infinite loop because the counter variable is not incremented during each loop cycle so
# always stays less than 5, keeping the conditional for the while loop True
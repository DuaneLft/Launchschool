# Explain why the code below prints different values for line 3 and 4

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29


# In the first line of code the reverse find is working on the return from the slice which is only 14 elements in
# length "for the fjords" and 'f' is found 5 spots back from the end.

# In the second line of code you are telling reverse search to look for 'f' from index 21 through 35 but it is looking at the entire
# text string and giving the index found based on the entire string
# Write Python code to replace all the : characters in the string below
# with + .

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = info.split(':')
new_info = '+'.join(new_info)
print(new_info)
# Also
# new_info = info.replace(':', '+')

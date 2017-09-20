"""
19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
"""

def add_is(str):
    if str[:2] != 'Is':
        str = 'Is' + str
    
    return str

print add_is('wynfrith')
print add_is("IsEmpty")
print add_is("I")

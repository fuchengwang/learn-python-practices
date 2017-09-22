"""
37. Write a Python program to display your details like name, age, address in three different lines.
"""

def personal_infos():
    name, age = 'wyn', 24
    address = 'hello'
    print 'name: %s\nage: %d\naddress: %s' % (name, age, address)

personal_infos()
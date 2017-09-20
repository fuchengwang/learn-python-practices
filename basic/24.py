"""
24. Write a Python program to test whether a passed letter is a vowel or not. 
"""

def is_vowel(letter):
    return letter.lower() in 'aeiou':

print is_vowel('o')
print is_vowel('b')


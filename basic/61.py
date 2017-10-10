"""
61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""

def print_converted_distance(feets):
    inches = feets * 12
    yards = feets / 3.0
    miles = feets / 5280.0

    fmt = "The distance of %d feets is %d inches or %.2f yards or %.2f miles"
    print(fmt % (feets, inches, yards, miles))


print_converted_distance(100)
"""
55. Write a Python to find local IP addresses using Python's stdlib
"""

# import urllib.request

# req = urllib.request.urlopen('http://localhost:8080')


import socket
print socket.getfqdn()
print socket.gethostbyname(socket.gethostname())
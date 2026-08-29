"""
RULES FOR PASSWORD:
-----------------------------------------------
- Must have length of at least 12
- Must have at least one uppercase (A-Z)
- Must have at least one lowercase (a-z)
- Must have at least one number (0-9)
- Must have at least one special character !@#$%^&*(){}<>/\
"""

import string

def checkpass(password):
    alert = []

    if len(password) < 12:
        alert.append("Password must be at least 12 characters")

    if not any(char.isupper() for char in password):
        alert.append("Password must contain at least one uppercase character")

    if not any(char.islower() for char in password):
        alert.append("Password must contain at least one lowercase character")

    if not any(char.isdigit() for char in password):
        alert.append("Password must contain at least one number character")

    if not any(char in string.punctuation for char in password):
        alert.append("Password must contain at least one symbol character")

    commonPasswords = {
        "123456", "password", "qwerty123", "admin", "111111", "222222", "abcdefghijklmnop", "ABCDEFGHIJKLMNOPQ", "baseball", "1111111111111", "apple", "hello"
        "10101010", "jennifer", "robert", "q1w2e3r4t5y6", "batman", "butterfly", "friends", "Password1", "newyork", "flower1", "october", "soccer10", "password11"
    }

    if(password in commonPasswords):
        alert.append("Password is commonly used")

    if len(alert) > 0:
        print("Password is not strong!\n")
        for message in alert:
            print("- ", message)
    else:
        print("Password is strong!")


password = input("Enter password: ")
checkpass(password)




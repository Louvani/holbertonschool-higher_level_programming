#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        character = ord(str[i])
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            character = ord(str[i]) - 32
        print("{:c}".format(character), end="")
    print()

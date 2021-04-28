#!/usr/bin/python3
def remove_char_at(str, n):
    aux = ""
    for i in range(len(str)):
        if i == n:
            continue
        aux += str[i]
    return aux

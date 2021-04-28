#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    import sys
    array = dir(hidden_4)
    for i in range(len(array)):
        if array[i][0] != '_':
            print(hidden[i])


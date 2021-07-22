#!/usr/bin/python3
''' Log parsing '''


import sys

file_size = 0
status_code = []
status_code_list = ["200", "301", "400", "401", "403", "404", "405", "500"]

for idx, line in enumerate(sys.stdin):
    words = line.split()
    file_size += int(words[-1])
    status_code.append(words[-2])
    if not idx + 1 % 10 and idx != 0:
        print('File size: {:d}'.format(file_size))
        file_size = 0
        for key in status_code_list:
            if key in status_code:
                print("{}: {:d}".format(key, status_code.count(key)))
        status_code = []

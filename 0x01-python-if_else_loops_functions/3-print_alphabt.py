#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet == 113 or alphabet == 101:
        continue
    print("{:c}".format(alphabet), end="")

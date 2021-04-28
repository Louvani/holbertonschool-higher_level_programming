#!/usr/bin/python3
for alpha in reversed(range(97, 123)):
    print("{:c}".format(alpha if alpha % 2 == 0 else alpha - 32), end="")

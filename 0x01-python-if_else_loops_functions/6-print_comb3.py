#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(0, 10):
        if num != num2 and num < num2:
            if (num * 10) + num2 < 89:
                print("{}{}, ".format(num, num2), end="")
            else:
                print("{}{}".format(num, num2))

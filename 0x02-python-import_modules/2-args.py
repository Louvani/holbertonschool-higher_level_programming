#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    leng = len(argv)
    if leng == 1:
        print("0 arguments.")
    elif leng == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(leng - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

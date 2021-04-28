#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    leng = len(argv)
    print("0 arguments." if leng == 1 else "{} arguments:".format(leng - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	num = 0
	try:
		for i in range(0, x):
			print("{:d}".format(my_list[i]), end="")
			num += 1
	except IndexError:
		pass
	print("")
	return num

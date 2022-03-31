from curses.ascii import ispunct
import sys
import re, string


if len(sys.argv) != 3 or sys.argv[2].isdigit() is False:
	print("ERROR")
	quit(0)

newList = re.split("[" + string.punctuation + " " + "]+", sys.argv[1])
treated_list = [x for x in newList if len(x) > int(sys.argv[2])]
print(treated_list)

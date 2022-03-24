import sys


def reverse(x):
    return x[::-1]


for entry in sys.argv:
    if entry == "exec.py":
        continue;
    print (reverse(entry).swapcase(), end=" ")
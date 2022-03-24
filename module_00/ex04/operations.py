import sys


def func_usage(error):
    if len(error) > 0:
        print(error, "\n")
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")


def operations(nb1, nb2):
    print("Sum : ".ljust(15), nb1 + nb2)
    print("Difference : ".ljust(15), nb1 - nb2)
    print("Product : ".ljust(15), nb1 * nb2)
    if nb1 is 0 or nb2 is 0:
        print("Quotient : ".ljust(15), "ERROR (div by zero)")
        print("Remainder : ".ljust(15), "ERROR (modulo by zero)")
    else:
        print("Quotient : ".ljust(15), nb1 / nb2)
        print("Remainder : ".ljust(15), nb1 % nb2)


if len(sys.argv) < 3:
    func_usage("")
elif len(sys.argv) > 3:
    func_usage("InputError: too many arguments")
elif sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False:
    func_usage("InputError: only numbers")
else:
    operations(int(sys.argv[1]), int(sys.argv[2]))

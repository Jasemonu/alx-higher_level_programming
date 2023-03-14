#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
argv_length = len(argv)-1
if argv_length == 0:
    print("0 arguments.")
elif argv_length == 1:
    print("1 argument:")
else:
    print("{} arguments:" .format(argv_length))
for i in range(argv_length):
    print("{} : {}".format(i + 1, argv[i+1]))

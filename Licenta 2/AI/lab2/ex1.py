import sys


def aduna(*args):
    s = 0
    for x in args:
        if not str(x).isdigit():
            return "Nu se poate face suma"
        s += int(x)
    return s


l = []
for i in range(1, len(sys.argv)):
    l.append(sys.argv[i])
print(aduna(*l))

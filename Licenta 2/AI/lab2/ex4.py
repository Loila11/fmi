l = [109, 5, 33, 91]

# a
l.sort(key=lambda x: str(x))
print(l)

# b
l.sort(key=lambda x: list(reversed(str(x))))
print(l)

# c
l.sort(key=lambda x: len(str(x)))
print(l)

# d
l.sort(key=lambda x: len(set(str(x))))
print(l)

# e
l = ["1+2+3","2-5","3+4","5*10"]
l.sort(key=lambda x: eval(x))
print(l)

# a
def calculeaza1(AuB, AiB, AmB):
    return AmB | AiB, AuB - AmB


print(calculeaza1({1, 2, 3, 4}, {1, 3}, {2}))


# b
def calculeaza2(AiB, AmB, BmA):
    return AmB | AiB, BmA | AiB


print(calculeaza2({1, 3}, {2}, {4}))

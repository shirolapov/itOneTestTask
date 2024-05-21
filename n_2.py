m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

count = sum([len(x) for x in m])
summary = sum([sum(x) for x in m])
avg = sum([x1 for x in m for x1 in x]) / sum([len(x) for x in m])
cus_tuple = tuple([x1 for x in m for x1 in x])

assert count == 14
assert summary == 264
assert avg == 18.857142857142858
assert cus_tuple == (11, 3, 5, 32, 17, 2, 87, 4, 44, 7, 8, 9, 11, 24)

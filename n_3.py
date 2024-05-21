a = [[1, 2, 3], [4, 5, 6]]
b = [dict([a for a in zip([f'k{i}' for i in range(1, len(x) + 1)], x)]) for x in a]

assert b == [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]

a1 = [1, 2, 3, 4, 5,7,8,9,10]
a2 = [4, 5, 6, 7, 8,10,9]
s1 = set(a1)
s2 = set(a2)
common = s1 & s2
result = tuple(sorted(common))
print(result)

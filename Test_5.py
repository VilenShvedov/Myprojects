kort_a = (1, 2, 3, 5, 8)
kort_b = (8, 2, 5)

#kort_a = list(kort_a)
#kort_b = list(kort_b)
#kort_a.extend(kort_b)
#rint(kort_a)



kort_a = (1, 2, 3, 5, 8)
kort_b = (8, 2, 5)

kort_a = list(kort_a)
for x in kort_b:
    kort_a.insert(2, x)
kort_a = tuple(kort_a)
print(kort_a)

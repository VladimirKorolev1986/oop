import math

coords1 = [1, 2, 2, 4]
coords2 = [3, 2, 3]

i = 0
for _, _ in zip(coords1, coords2):
    coords2[i] = coords1[i]
    i+=1

print(coords2)
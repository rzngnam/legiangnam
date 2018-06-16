import math
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
z = []


def xyz():
    for i in range(len(x)):
        y.append((math.pi / 2) + x[i])
        z.append((math.cos(x[i])) - (math.sin(x[i])))
    return x , y, z

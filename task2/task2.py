def detecter(x, y, radius, x2, y2):
    if (x2 - x) ** 2 + (y2 - y) ** 2 < radius ** 2:
        return 1
    if (x2 - x) ** 2 + (y2 - y) ** 2 == radius ** 2:
        return 0
    if (x2 - x) ** 2 + (y2 - y) ** 2 > radius ** 2:
        return 2

def circle(file):
    numbers = []
    with open(s) as f:
        for line in f:
            x1y1r = [float(i) for i in line.split()]
            numbers.append(x1y1r)
    return numbers

def coordinates(file):
    points = []
    with open(s) as f:
        for line in f:
            x2y2 = [float(i) for i in line.split()]
            points.append(x2y2)
    return points

s = input()
x1y1, r = circle(s)
x1, y1 = [float(i) for i in x1y1]

n = input()
points = coordinates(n)

for point in points:
    x2, y2 = [float(i) for i in point]
    print(detecter(x1, y1, *r, x2, y2))
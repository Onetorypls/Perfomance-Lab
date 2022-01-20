n, m = [int(i) for i in input().split()]
a = [int(i) for i in range(1, n + 1)] * m
res = []
for i in range(0, len(a), (m - 1)):
    res.append(a[i])
    if a[i + m - 1] == 1:
        break
print(*res, sep='')


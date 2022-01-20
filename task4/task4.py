def avg(num):
    return round(sum(num)/len(num))

def rounding(func, num):
    counter = 0
    s = func(num)
    for n in num:
        while n != s:
            if n < s:
                n += 1
                counter += 1
            else:
                n -= 1
                counter += 1
    return counter

numbers = []
s = input()
with open(s) as f:
    for line in f:
        numbers.append(int(line))
print(rounding(avg, numbers))
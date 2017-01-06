a = 1
b = 1
cnt = 0

for _ in range(1000):
    aa = a + 2 * b
    bb = a + b
    a = aa
    b = bb
    if len(str(a)) > len(str(b)):
        cnt += 1
print cnt

ans = 0

for a in range(1, 100):
    for b in range(1, 100):
        cand = 0
        powstr = str(a**b)

        for c in powstr:
            cand += int(c)

        if ans < cand:
            ans = cand
print ans

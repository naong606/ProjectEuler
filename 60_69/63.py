from math import log, log10
MAX = int(log(10)/(log(10/9))+1)

ans = 0
for n in range(1, MAX):
    for c in range(1, 10):
        lg = n * log10(c)
        if lg >= n-1 and lg < n:
            print (n, c, c**n)
            ans += 1
print(ans)

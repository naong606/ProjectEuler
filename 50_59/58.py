import math

cnt = 0
n = 0
MAX = 100000

isPrime = [True] * MAX
isPrime[0] = isPrime[1] = False
for i in range(2, int(math.sqrt(MAX))):
    if isPrime[i]:
        for j in range(2*i, MAX, i):
            isPrime[j] = False
primes = []
for i in range(MAX):
    if isPrime[i]:
        primes.append(i)

def isp(n):
    for p in primes:
        if p > n or n%p == 0:
            if n == p:
                return True
            else:
                return False
    return True

while True:
    n += 1
    m = (2*n+1)**2
    for i in range(1, 4):
        if isp(m-i*2*n):
            cnt += 1
    if cnt*10 < 4*n+1:
        break
    print "{0}: {1}".format(n, cnt)
print cnt

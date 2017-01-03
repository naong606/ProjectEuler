import math
import itertools

MAX = 1000
isPrime = [True] * MAX
isPrime[0] = isPrime[1] = False
for i in range(2, int(math.sqrt(MAX))+1):
    if isPrime[i]:
        for j in range(2*i, MAX, i):
            isPrime[j] = False
primes = []
for i in range(2, MAX):
    if isPrime[i]:
        primes.append(i)

def isp(n):
    if n < MAX:
        return isPrime[n]
    else:
        for p in primes:
            if n%p==0:
                return False
        return True

graph = []
for _ in range(len(primes)):
    graph.append([False]*len(primes))

for i in range(len(primes)):
    p1 = primes[i]
    for j in range(len(primes)):
        p2 = primes[j]
        graph[i][j] = isp(int(str(p1)+str(p2))) and isp(int(str(p2)+str(p1)))
    graph[i][i] = True

for i in range(len(primes)):
    if graph[i].count(True) >= 4:
        print primes[i]
'''
for comb in itertools.combinations(range(len(primes)), 4):
    try:
        for i in comb:
            for j in comb:
                assert graph[i][j]
        for i in comb:
            print primes[i],
        print
    except:
        None'''

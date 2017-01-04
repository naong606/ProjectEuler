import math
import itertools

MAX = 10000
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

pairs = []
for i in range(len(primes)):
    p1 = primes[i]
    for j in range(i+1, len(primes)):
        p2 = primes[j]
        graph[i][j] = isp(int(str(p1)+str(p2))) and isp(int(str(p2)+str(p1)))
        if graph[i][j]:
            pairs.append([i, j])

triples = []
for p in pairs:
    for i in range(p[1]+1, len(primes)):
        flag = True
        for e in p:
            if not graph[e][i]:
                flag = False
                break
        if flag:
            triples.append(p+[i])

quart = []
for p in triples:
    for i in range(p[1]+1, len(primes)):
        flag = True
        for e in p:
            if not graph[e][i]:
                flag = False
                break
        if flag:
            quart.append(p+[i])

pent = []
for p in quart:
    for i in range(p[1]+1, len(primes)):
        flag = True
        for e in p:
            if not graph[e][i]:
                flag = False
                break
        if flag:
            pent.append(p+[i])


for p in pent:
    print("({0}, {1}, {2}, {3}, {4})".format(primes[p[0]], primes[p[1]], primes[p[2]], primes[p[3]], primes[p[4]]))

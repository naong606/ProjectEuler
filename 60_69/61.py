poly = []
for c in range(3, 9):
    a = c-2
    b = -c+4
    for n in range(1000):
        res = n*(a*n+b)//2 
        if res >= 10000:
            break
        elif res < 1000:
            continue
#        print("{0},{1} : {2}".format(c, n, res))
        poly.append((c, res))

adj = []

for i in range(len(poly)):
    tmp = []
    for j in range(len(poly)):
        if i != j and poly[i][0] != poly[j][0] and poly[i][1]%100 == poly[j][1]//100:
            tmp.append(j)
    adj.append(tmp)

start = -1
visited = [False]*len(poly)
polychk = [False]*6
polychk[0] = True
ans = 0

def dfs(v):
    global start, ans, visited, polychk
    for there in adj[v]:
#        print(polychk, there, start)
        if all(polychk) and there is start:
            print(poly[there])
            return True
        elif not visited[there] and not polychk[poly[there][0]-3]:
            visited[there] = True
            polychk[poly[there][0]-3] = True
            ans += poly[there][1]
#            print("in"+str(poly[there]))
            if dfs(there):
                print(poly[there])
                return True
#            print("out"+str(poly[there]))
            visited[there] = False
            polychk[poly[there][0]-3] = False
            ans -= poly[there][1]
    return False

for i in range(len(poly)):
    if poly[i][0] is not 3:
        break

    start = i
    visited[i] = True
    ans = poly[i][1]
    if dfs(i):
        print(ans)
        break
    visited[i] = False
    

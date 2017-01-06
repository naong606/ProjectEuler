cnt = 0

def revInt(n):
    return int(str(buf)[::-1])

for n in range(10000):
    buf = n
    for i in range(50):
        buf = buf + revInt(buf)
        if (buf == revInt(buf)):
            cnt += 1
            break
print 10000-cnt

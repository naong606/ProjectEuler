with open("p059_cipher.txt") as cipher:
    code = cipher.read()
    chars = code.split(',')
    chars = map(lambda x: int(x), chars)
    
    for i in range(ord('a'), ord('z')+1):
        for j in range(ord('a'), ord('z')+1):
            for k in range(ord('a'), ord('z')+1):
                pw = (i, j, k)
                res = ""
                for n in range(len(chars)):
                    res += chr(chars[n] ^ pw[n%3])
                if res.find(' the ') != -1:
                    print res
                    asciisum = 0
                    for c in res:
                        asciisum += ord(c)
                    print asciisum

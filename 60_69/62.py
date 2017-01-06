cube_digits = {}

def cnt_digits(n):
    ret = [0]*10
    while n > 0:
        ret[n%10] += 1
        n //= 10
    return tuple(ret)

for n in range(10000):
    n_tuple = cnt_digits(n**3)
    if n_tuple in cube_digits:
        cube_digits[n_tuple][0] += 1
    else:
        cube_digits[n_tuple] = [1, n]

ans = min([cube_digits[k][1] for k in cube_digits if cube_digits[k][0] == 5])
print(ans**3)

byk = int(input())
for i in range(byk):
    lk , pk = map(int,input().split())
    r1 = 12
    r2 = -1*((2*lk + 2*pk)*2)
    r3 = lk*pk
    x1 = (r2 + (((r2**2)-(4*r1*r3))**(1/2)))/(2*r1)
    x2 = (r2 - (((r2 ** 2) - (4 * r1 * r3)) ** (1 / 2))) / (2 * r1)
    hls = min(abs(x1),abs(x2))
    print((lk-(2*hls))*(pk-(2*hls))*hls)

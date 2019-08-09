dt = input().split()
height = int(dt[0])
bil = 2**(height+1)-1
if len(dt)==1 :
    print(bil)
else :
    arah = dt[1]
    hls = 0
    for i in range(1,len(arah)):
        hls += 2**i
    hls =  bil - hls
    kkk = 1
    byk = 2**len(arah)
    kk = byk
    for i in range(len(arah)):
        if arah[i] == 'R' :
            kkk += int(byk/2)
        byk = int(byk/2)
    print(hls-kkk)

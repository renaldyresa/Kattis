byk = int (input())
for i in range(byk):
    data = list(map(int,input().split()))
    hls = 0
    for j in range(1,len(data)-1):
        hl = data[j]-data[j-1]*2
        if hl < 0 :
            hls += 0
        else:
            hls += hl
    print(hls)

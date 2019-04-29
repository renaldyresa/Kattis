byk = int(input())
kk = 1
while byk != 0 :
    ak = int(input())
    data = list(map(int, input().split()))
    hls = []
    for i in  range(len(data)):
        if data[i] not in hls :
            hls.append(data[i])
        else :
            hls.remove(data[i])
    print("Case #"+str(kk)+":",hls[0])
    kk += 1
    byk -= 1

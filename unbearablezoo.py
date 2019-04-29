q = 1
while True :
    byk = int(input())
    if byk == 0 :
        break
    data = []
    data1 = []
    for i in range(byk) :
        dt = list(map(str,input().split()))
        kt = dt[len(dt) - 1].lower()
        data.append(kt)
        if kt not in data1 :
            data1.append(kt)
    data.sort()
    data1.sort()
    print("List "+str(q)+":")
    for i in range(len(data1)):
        print(data1[i],"|",end=' ')
        hls = 0
        for j in range(len(data)):
            if data1[i] == data[j] :
                hls+=1
        print(hls)
    q+=1


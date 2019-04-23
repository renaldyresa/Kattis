while True :
    byk = int(input())
    if byk==0:
        break
    hls = []
    hls1 = []
    for i in range (byk):
        kl = input()
        hls1.append(kl)
        data = kl.split(" ")
        for j in range(len(data)):
           if j ==0 :
               continue
           if data[j] not in hls :
               hls.append(data[j])
    hls.sort()
    hls1.sort()
    for i in range(len(hls)):
        print(hls[i],end=" ")
        for j in range(len(hls1)):
            if hls[i] in hls1[j]:
                print(hls1[j].split(" ")[0],end=" ")
        print("")
    print("")        
        

while True :
    byk = int(input())
    if byk == 0 :
        break
    hlss = ""
    hl = -1
    for i in range(byk):
        kt = input()
        hls = 0
        for j in range(1,len(kt)):
            if kt[j]=='a' or kt[j]=='i' or kt[j]=='u' or kt[j]=='e' or kt[j]=='o' or kt[j]=='y':
                if kt[j-1] == kt[j]:
                    hls+=1
        if hl < hls :
            hl = hls
            hlss=kt
    print(hlss)

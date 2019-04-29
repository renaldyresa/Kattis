byk = int(input())
for i in range(byk):
    ak = input()
    hls = ""
    hl = 0
    for i in range(len(ak)-1,-1,-1):
        if ak[i] != "0" and hl == 0:
            aa = int(ak[i])-1
            hls += str(aa)
            hl = 1
        else :
            hls += ak[i]
    hls3 = ""
    for i in range(len(hls)-1,-1,-1):
        hls3 += hls[i]
    print(int(hls3))

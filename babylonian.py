for i in range(int(input())):
    dt =  list(map(str,input().split(",")))
    hls = 0
    byk = len(dt)
    for j in range(byk):
        if len(dt[j])!=0 :
            hls += int(dt[j])*(60**(byk-j-1))
    print(hls)

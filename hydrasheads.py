while True :
    n,m = map(int,input().split())
    if n==0 and m==0 :
        break
    hls = 0
    while True :
        if n==0 and m==0 :
            break
        if n%2!=0 or m>3:
            m -=2
            n+=1
            hls +=1
        elif n>1:
            n -= 2
            hls +=1
        else :
            m+=1
            hls+=1
    print(hls)

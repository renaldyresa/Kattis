while True :
    width = int(input())
    if width == 0 :
        break
    hls1,hls2 = 0,0
    panjang = 0
    lebar = 0
    while True :
        p,l = map(int,input().split())
        if p==-1 or l==-1 :
            if hls1 < panjang:
                hls1 = panjang
            hls2 += lebar
            break
        if panjang + p <= width :
            panjang += p
            if lebar < l :
                lebar = l
        else :
            if hls1<panjang :
                hls1 = panjang
            hls2 += lebar
            panjang = p
            lebar = l
    print(hls1,"x",hls2)


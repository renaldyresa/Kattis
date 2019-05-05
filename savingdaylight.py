while True :
    try:
        bulan,tgl,thn,jam1,jam2 =map(str,input().split())
        ak1 = list(map(int,jam1.split(":")))
        ak2 = list(map(int,jam2.split(":")))
        hls2 = ak2[1]-ak1[1]
        hls1 = ak2[0]-ak1[0]
        if hls2 < 0 :
            hls2 = 60+hls2
            hls1 -=1
        print(bulan,tgl,thn,hls1,'hours',hls2,'minutes')
    except EOFError :
        break

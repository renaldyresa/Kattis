byk = int(input())
for j in range(byk):
    hari , bulan = map(int,input().split())
    data = [int(x) for x in input().split()]
    hls = 0
    ak = 0
    for i in data :
        hh = (i + ak) % 7
        if i > 12 and ((ak+12)%7==5):
            hls += 1
        ak = hh
    print(hls)

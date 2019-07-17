ak = int(input())
hls = True
awal,akhir = map(int,input().split())
for i in range(ak-1):
    a,b = map(int,input().split())
    if awal<=b and akhir>=a :
        if awal<=a :
            awal = a
        if akhir >= b :
            akhir = b
    else :
        hls = False
print( "gunilla has a point" if hls else "edward is right" )

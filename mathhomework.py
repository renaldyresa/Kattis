b,c,d,l = map(int,input().split())
byk = min(b,c,d)
hls = True
ak = 0
while True :
    if ak*byk>l:
        break
    ak += 1
for i in range(ak):
    hh = b*i
    if hh > l :
        break
    for j in range(ak):
        hhh = c*j + hh
        if hhh > l :
            break
        for k in range(ak):
            if hhh+d*k > l :
                break
            if b*i+c*j+d*k==l:
                print(i,j,k)
                hls = False
if hls :
    print("impossible")

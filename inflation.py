byk = int(input())
data = sorted([int(x) for x in input().split()])
hls = True
hl = byk
for i in range(1,byk+1):
    if data[i-1]>i:
        hls =False
        break
    else :
        hl = min(hl,data[i-1]/i)
if hls :
    print(hl)
else :
    print("impossible")

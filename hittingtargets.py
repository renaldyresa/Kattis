import math
def kotak(a,b,c,d,x,y):
    if (a<=x and x<=c)and (b<=y and y<=d):
        return 1
    else :
        return 0
def ling(a,b,r,x,y):
    korx = abs(x-a)
    kory = abs(y-b)
    jar = math.sqrt((korx**2)+(kory**2))
    if jar<=r :
        return 1
    else:
        return 0

byk = int(input())
data = []
for i in range(byk):
    data.append(input())
byk2 = int(input())
for i in range(byk2):
    kdx,kdy = map(int,input().split())
    hls = 0
    for j in data:
        dt = j.split()
        if dt[0]=="rectangle" :
            hls+=kotak(int(dt[1]),int(dt[2]),int(dt[3]),int(dt[4]),kdx,kdy)
        else :
            hls+=ling(int(dt[1]),int(dt[2]),int(dt[3]),kdx,kdy)
    print(hls)

def rms (a,b):
    if a==b :
       return a
    if a > b :
        return rms(a-b,b)
    else :
        return rms(a,b-a)

byk = int(input())
data = list(map(int,input().split()))
for i in range (1,byk):
    hls = rms(data[0],data[i])
    dt1 = int(data[0]/hls)
    dt2 = int(data[i]/hls)
    print(str(dt1)+"/"+str(dt2))

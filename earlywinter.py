tahun , dm = map(int,input().split())
data = [dm]+[int(x) for x in input().split()]
hls = -1
for i in range(1,tahun+1):
    if dm >= data[i] :
        hls = i
        break
print("It had never snowed this early!" if hls==-1 else "It hadn't snowed this early in "+str(hls-1)+" years!")

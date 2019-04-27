byk = int(input())
data = list(map(int,input().split()))
hls = 0
for i in range (byk):
    if data[i] < 0 :
        rms = data[i]*-1
        hls += rms
print(hls)

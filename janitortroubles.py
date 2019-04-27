import math
data = list(map(int,input().split()))
rms = 0
for i in data :
    rms += i ;
rms = rms/2
hls = math.sqrt((rms-data[0])*(rms-data[1])*(rms-data[2])*(rms-data[3]))
print(hls)

import math
def distance(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
byk = int(input())
data = [True for x in range(byk)]
datain = []
for i in range(byk):
    datain.append(list(map(float,input().split())))
hls = [0 for i in range(byk)]
hls[0] = 0
data[0] = False
for i in range(1,byk):
    terbaik = -1
    for j in range(byk):
        if  data[j] and (terbaik == -1 or distance(datain[hls[i-1]], datain[j]) < distance(datain[hls[i-1]], datain[terbaik])):
            terbaik = j
    hls[i] = terbaik
    data[terbaik] = False
for i in hls :
    print(i)

byk = int(input())
hls1 = []
hls = []
while byk!=0 :
    kl = str(input())
    n ,m = map(str,kl.split())
    hls1.append(kl)
    if n not in hls :
        hls.append(n)
    else :
        hls1.remove(kl)
    byk -=1

for i in range(12):
    print(hls1[i])

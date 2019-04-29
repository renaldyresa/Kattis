import math
data=[]
for i in range(int(3)):
    data.append(list(map(int,input().split())))
l = 0
p = 0
hls = 0.0
for k in range(1,int(10)):
    h = 0
    for i in range(int(3)):
        for j in range(int(3)):
            if data[i][j] == k :
                if k>1 :
                    if i==l or p==j :
                        if i-l == 0 :
                            aa = p-j
                            if aa<0 :
                                hls += aa*(-1)
                            else :
                                hls +=aa
                        else :
                            aa = i-l
                            if aa < 0:
                                hls += aa * (-1)
                            else:
                                hls += aa
                    else :
                        aa = i-l
                        bb = p-j
                        if aa<0 :
                            aa = aa*(-1)
                        if bb<0 :
                            bb = bb*(-1)
                        if (aa+bb)%2 == 0 :
                            hls += math.sqrt(2)*((aa+bb)/2)
                        else :
                            hls += math.sqrt(5)
                l = i
                p = j
                h=1
                break
        if h == 1 :
            break
print(hls)

a,b,c = map(int,input().split())
data1 = []
data2 = []
min = 100
max = 0
for i in range(int(3)):
    n,m = map(int,input().split())
    if n<min :
        min = n
    if m >max :
        max=m
    data1.append(n)
    data2.append(m)
hls = 0
for i in range(min+1,max+1):
    hl = 0
    for j in range(int(3)):
        if data1[j] < i and data2[j] >= i :
            hl +=1
    if hl == 1 :
        hls += a
    elif hl == 2 :
        hls += b*2
    elif hl ==3 :
        hls += c*3
print(hls)

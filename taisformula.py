byk = int(input())
hls = 0.0
dt1 = 0.0
dt2 = 0.0
for i in range(byk):
    n,m = map(float,input().split())
    if i != 0 :
        hls = hls+float((((dt1+m)/float(2))*(n-dt2))/1000)
    dt1 = m
    dt2 = n
print(hls)

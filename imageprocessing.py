h,w,n,m = map(int,input().split())
data1 = []
data2 = []
for i in range(h):
    data1.append(list(map(int,input().split())))
for i in range(n):
    data2.append(list(map(int,input().split())))
hls = []
for i in range(h-n+1):
    dt = []
    for j in range(w-m+1):
        hh = []
        for l in range(n):
            for k in range(m):
                hh += [data1[i+l][j+k]*data2[n-1-l][m-1-k]]
        print(sum(hh),end=" ")
    print()

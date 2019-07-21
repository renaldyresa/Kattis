n , l  = map(int,input().split())
hls = 0
k = 0
for i in range(n):
    d,r,g = map(int,input().split())
    hls += d - k
    if (hls)%(r+g) <= r :
        hls += r-(hls)%(r+g)
    k = d
print(hls+(l-k))

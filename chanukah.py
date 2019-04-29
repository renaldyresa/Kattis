byk = int(input())
for i in range (byk):
    n,m = map(int,input().split())
    hls = int(m/2*(2+(m-1)))+m
    print(n,hls)

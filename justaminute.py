byk = int(input())
hls1 = 0
hls2 = 0
while byk>0 :
    dt1 ,dt2 = map(int, input().split())
    hls1 += dt1
    hls2 += dt2/60
    byk -= 1
if hls2 <= hls1 :
    print("measurement error")
else :
    print(hls2/hls1)

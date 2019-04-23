byk = int(input())
hls1 = 1 
hls2 = 0
for i in range(byk):
    a = hls1
    hls1 = hls2
    hls2 = a+hls2
print(hls1," ",hls2)

byk = int(input())
hls1 = 0
hls = 0
data = []
for i in range(byk):
    data.append(int(input()))
data1 = []
data.sort(reverse=True)
for i in range(byk):
    hls1 = hls1+data[i]
    if i%3 == 2:
        data1.append(data[i])
        data1.sort()
        hls = hls+data1[0]
        data1.clear()
    else:
        data1.append(data[i])
print(hls1-hls)

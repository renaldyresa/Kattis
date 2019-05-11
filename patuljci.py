data = []
for i in range(9):
    data.append(int(input()))
data1 = data.copy()
data1.sort()
k1 = 8
k2 = 7
i = 0
while True :
    hls = 0
    for j in range(9):
        if k1 != j and k2!=j:
            hls+=data1[j]
        if hls>100 :
            break
    if hls == 100 :
        break
    k2 -= 1
    if k2 < 0:
        k1 -= 1
        k2 = k1 - 1
    if k1<0:
        break
for i in data :
    if i != data1[k1] and i != data1[k2]:
        print(i)

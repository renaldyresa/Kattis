data = list(map(int,input().split()))
i = 0
j = 1
dt = data.copy()
dt.sort()
while True :
    if data[i]>data[j]:
        bt = data[i]
        data[i] = data[j]
        data[j] = bt
        for k in range(len(data)):
            print(data[k], end=' ')
        print()
    i +=1
    j +=1
    if data == dt :
        break
    if j == 5 :
        i =0
        j = 1

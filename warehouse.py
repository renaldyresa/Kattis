byk = int(input())
for i in range(byk):
    data1 = []
    data2 = []
    ak = int(input())
    for j in range(ak):
        brg, cou = map(str,input().split())
        if brg not in data1 :
            data1.append(brg)
            data2.append(int(cou))
        else :
            data2[data1.index(brg)]+=int(cou)
    for j in range(len(data1)-1):
        for k in range(j+1,len(data1)):
            if data2[j]<data2[k] :
                bt1 = data2[j]
                data2[j] = data2[k]
                data2[k] = bt1
                bt2 = data1[j]
                data1[j] =data1[k]
                data1[k] = bt2
            if data2[j]==data2[k] and data1[j]>data1[k]:
                bt1 = data2[j]
                data2[j] = data2[k]
                data2[k] = bt1
                bt2 = data1[j]
                data1[j] = data1[k]
                data1[k] = bt2
    print(len(data1))
    for j in range(len(data1)):
        print(data1[j],data2[j])

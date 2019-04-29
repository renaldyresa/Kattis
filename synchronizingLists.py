while True :
    byk = int (input())
    if byk == 0 :
        break
    data1=[]
    data2=[]
    data3=[]
    for i in range(byk):
        d = int(input())
        data1.append(d)
        data3.append(d)
    for i in range(byk):
        da = int(input())
        data2.append(da)
    data3.sort()
    data2.sort()
    for i in range(byk):
        a = data3.index(data1[i])
        print(data2[a])
    print("")

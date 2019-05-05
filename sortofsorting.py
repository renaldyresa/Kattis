while True:
    byk = int(input())
    if byk == 0 :
        break
    data = []
    for i in range(byk):
        data.append(input())
    data.sort(key=lambda x:x[0:2])
    for i in data :
        print(i)
    print()

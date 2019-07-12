for i in range(int(input())):
    data = list(map(int,input().split()))
    data.pop(0)
    hl = True
    hh = data[1]-data[0]
    for j in range(1,len(data)-1) :
        if data[j+1]-data[j] != hh :
            hl = False
            break
    if hl :
        print("arithmetic")
        continue
    data.sort()
    hl = True
    hh = data[1] - data[0]
    for j in range(1, len(data) - 1):
        if data[j + 1] - data[j] != hh:
            hl = False
            break
    if hl:
        print("permuted arithmetic")
        continue
    else :
        print("non-arithmetic")

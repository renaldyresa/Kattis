def main ():
    data1 = []
    data2 = []
    ak = int(input())
    dt = list(map(int,input().split()))
    for i in dt :
        if i not in data1 :
            data1.append(i)
            data2.append(0)
        else :
            data2[data1.index(i)] += 1
    if min(data2) == 0 :
        hl = 0
        for i in range(len(data2)):
            if data2[i] == 0 :
                if hl < data1[i] :
                    hl = data1[i]
        print(dt.index(hl)+1)
    else :
        print("none")

main()

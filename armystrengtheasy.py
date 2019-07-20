for i in range(int(input())):
    input()
    g1 , g2 = map(int,input().split())
    data = [int(x) for x in input().split()]
    data1 = [int(x) for x in input().split()]
    data.sort()
    data1.sort()
    while True :
        if len(data) == 0 or len(data1)==0:
            break
        if data1[0] <= data[0] :
            data1.remove(data1[0])
        else :
            data.remove(data[0])
    if len(data1) == 0 :
        print("Godzilla")
    elif len(data) == 0 :
        print("MechaGodzilla")
    else :
        print("uncertain")

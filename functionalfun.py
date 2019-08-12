while True :
    try:
        bijec,notaf,inj = True,False,True
        domain = input().split()[1:]
        codomain = input().split()[1:]
        data1,data2 = [],[]
        for i in range(int(input())):
            dt = input().replace(" ","").split("->")
            if dt[0] not in data1 and notaf==False:
                data1.append(dt[0])
                if dt[1] not in data2 :
                    data2.append(dt[1])
                else :
                    inj = False
            else :
                notaf = True
        if len(data1)==len(data2)==len(codomain):
            print("bijective")
        elif notaf :
            print("not a function")
        elif len(data2)==len(codomain):
            print("surjective")
        elif inj :
            print("injective")
        else :
            print("neither injective nor surjective")

    except EOFError :
        break

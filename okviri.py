kt = input()
k = 0
t = True
for i in range(5):
    for j in range(len(kt)):
        if (j+1) % 3 != 0 :
            if i==0 :
                print("..#.",end='')
            elif i==1 :
                print(".#.#",end='')
            elif i==2 :
                if t :
                    print("#."+kt[k]+".",end='')
                else :
                    print("*."+kt[k]+".",end='')
                    t = True
                k += 1
            elif i == 3 :
                print(".#.#",end='')
            else :
                print("..#.", end='')
        else :
            if i==0 :
                print("..*.",end='')
            elif i==1 :
                print(".*.*",end='')
            elif i==2 :
                print("*."+kt[k]+".",end='')
                t = False
                k += 1
            elif i == 3 :
                print(".*.*",end='')
            else :
                print("..*.", end='')
    if i!=2 :
        print(".")
    else :
        if t :
            print("#")
        else :
            print("*")

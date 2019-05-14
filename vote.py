byk = int(input())
for i in range(byk):
    data = []
    ak = int(input())
    jum = 0
    max = 0
    for j in range(ak):
        sur = int(input())
        if j == 0 :
            max=sur
        else :
            if max < sur :
                max = sur
        jum += sur
        data.append(sur)
    ll = 0
    hl = False
    for j in range(len(data)) :
        if max == data[j] :
            akk = j+1
            ll += 1
        if ll == 2 :
            hl = True
            break
    if hl :
        print("no winner")
    else :
        if jum/2 < max :
            print("majority winner",akk)
        else :
            print("minority winner",akk)

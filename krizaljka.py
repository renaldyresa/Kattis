kt1,kt2 = map(str,input().split())
h = 0
for i in range(len(kt1)):
    for j in range (len(kt2)):
        if kt1[i] == kt2[j] :
            h = 1
            break
    if h == 1 :
        break
q = 0
w = 0
for l in range(len(kt2)):
    for k in range(len(kt1)):
        if l== j and k==i :
            print(kt1[q],end='')
            q += 1
            w += 1
        elif l == j :
            print(kt1[q],end='')
            q += 1
        elif k == i :
            print(kt2[w],end='')
            w +=1
        else :
            print('.',end='')
    print()

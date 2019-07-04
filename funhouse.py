ak = 1
while True :
    l,p = map(int,input().split())
    if l==0 or p==0 :
        break
    data=[]
    hh = True
    for i in range(p):
        dt = list(input())
        for j in range(l) :
            if hh and dt[j]=='*':
                awal = [i,j]
                hh = False
        data.append(dt)
    ar = ['u','t','s','b']
    if awal[0] == 0 :
        arah = ar[2]
    elif awal[0] == p-1 :
        arah = ar[0]
    elif awal[1] == 0 :
        arah = ar[1]
    else :
        arah = ar[3]
    hh = True
    while hh :
        if arah == 's' :
            for i in range(awal[0],p):
                aa = data[i][awal[1]]
                if  aa != '.' and aa !='*'and i!=awal[0]:
                    awal[0] = i
                    if aa == 'x' :
                        data[awal[0]][awal[1]] = '&'
                        hh = False
                    elif aa == '/' :
                        arah = ar[3]
                    else :
                        arah = ar[1]
                    break
        elif arah == 'u' :
            for i in range(awal[0],-1,-1):
                aa = data[i][awal[1]]
                if aa != '.' and aa !='*' and i!=awal[0]:
                    awal[0] = i
                    if aa == 'x':
                        data[awal[0]][awal[1]] = '&'
                        hh = False
                    elif aa == '/':
                        arah = ar[1]
                    else:
                        arah = ar[3]
                    break
        elif arah == 't' :
            for i in range(awal[1],l):
                aa = data[awal[0]][i]
                if aa != '.' and  aa !='*' and i!=awal[1]:
                    awal[1] = i
                    if aa == 'x':
                        data[awal[0]][awal[1]] = '&'
                        hh = False
                        break
                    elif aa == '/':
                        arah = ar[0]
                    else:
                        arah = ar[2]
                    break
        else :
            for i in range(awal[1],-1,-1):
                aa = data[awal[0]][i]
                if aa != '.' and aa !='*' and i!=awal[1]:
                    awal[1] = i
                    if aa == 'x':
                        data[awal[0]][awal[1]] = '&'
                        hh = False
                        break
                    elif aa == '/':
                        arah = ar[2]
                    else:
                        arah = ar[0]
                    break
    print("HOUSE",ak)
    for i in range(p):
        for j in range(l) :
            print(data[i][j],end='')
        print()
    ak += 1

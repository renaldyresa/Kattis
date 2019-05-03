o = 0
while True :
    byk = int(input())
    if byk == 0 :
        break
    if o != 0 :
        print()
    err = 0
    h_err = False
    for i in range(byk):
        kt = list(map(str,input().split()))
        if kt[0]=='#':
            l = 1
        else :
            l = 0
        er = 0
        for j in range(1,len(kt)):
            if i == 0 :
                err +=int(kt[j])
            er += int(kt[j])
            if l == 1 :
                print('#'*int(kt[j]),end='')
                l = 0
            else :
                print('.'*int(kt[j]),end='')
                l= 1
        print()
        if er != err :
            h_err=True
    if h_err :
        print("Error decoding image")
    o+=1

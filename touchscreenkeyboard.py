huruf1 = "-qwertyuiop-asdfghjkl--zxcvbnm"
byk = int(input())
for i in range(byk):
    kata,ak = map(str,input().split())
    ak = int(ak)
    data = []
    for j in range(ak):
        kt= input()
        jarak = 0
        for k in range(len(kata)):
            if kata[k] != kt[k] :
                gol1, gol2 = 0, 0
                aa = huruf1.index(kata[k])
                if aa > 20 :
                    gol1 = 2
                elif aa >10 :
                    gol1 = 1
                else :
                    gol1 = 0
                bb = huruf1.index(kt[k])
                if bb > 20 :
                    gol2 = 2
                elif bb >10 :
                    gol2 = 1
                else :
                    gol2 = 0
                jarak += abs((aa%11)-(bb%11))+ abs(gol1-gol2)
        data.append([kt,jarak])
    data.sort()
    data.sort(key=lambda x : x[1])
    for j in data :
        print(j[0],j[1])

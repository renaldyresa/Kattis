def hitung(ak):
    i = 0
    while True :
        k = 2**i
        if k+k >= ak :
            return i
        i+=1

byk = int(input())
if byk<=3 :
    print(byk)
elif byk==4 :
    print(byk-1)
else :
    print(hitung(byk)+2)

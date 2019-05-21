import sys
data = {}
dd = True
for inp in sys.stdin :
    if dd :
        if inp=="\n":
            dd = False
        else  :
            dt, isi = map(str,inp.split())
            data[isi]= dt
    else :
        aa = inp.split()[0]
        try:
            print(data[aa])
        except:
            print("eh")

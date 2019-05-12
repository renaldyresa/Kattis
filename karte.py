kartu = input()
data = []
p,k,h,t = 13,13,13,13
hls = True
for i in range(0,len(kartu),3):
    kt = kartu[i:i+3]
    if kt not in data :
        data.append(kt)
        if kt[0]=="P":
            p -=1
        if kt[0] == "K":
            k -= 1
        if kt[0] == "H":
            h -= 1
        if kt[0] == "T":
            t -= 1
    else :
        hls = False
        break
if hls :
    print(p,k,h,t)
else :
    print("GRESKA")

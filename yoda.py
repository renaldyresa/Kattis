ak1 = input()
ak2 = input()
tak1 = len(ak1)
tak2 = len(ak2)
hls1 = ""
hls2 = ""
if tak1<tak2:
    hh = tak2-tak1
    hls2 += ak2[0:hh]
    j = hh
    for i in range(tak1):
        if ak1[i] < ak2[j]:
            hls2+=ak2[j]
        elif ak1[i] > ak2[j]:
             hls1+=ak1[i]
        else:
            hls2+=ak2[j]
            hls1+=ak1[i]
        j+=1
else :
    hh = tak1-tak2
    hls1 += ak1[0:hh]
    j = hh
    for i in range(tak2):
        if ak1[j] < ak2[i]:
            hls2+=ak2[i]
        elif ak1[j] > ak2[i]:
            hls1+=ak1[j]
        else:
            hls2+=ak2[i]
            hls1+=ak1[j]
        j+=1
if hls1=='':
    print("YODA")
else :
    print(int(hls1))
if hls2=='':
    print("YODA")
else :
    print(int(hls2))

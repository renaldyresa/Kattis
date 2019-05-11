data =  {"**** ** ** ****" : '0',
         "  *  *  *  *  *" : '1',
         "***  *****  ***" : '2',
         "***  ****  ****" : '3',
         "* ** ****  *  *" : '4',
         "****  ***  ****" : '5',
         "****  **** ****" : '6',
         "***  *  *  *  *" : '7',
         "**** ***** ****" : '8',
         "**** ****  ****" : '9',
        }
dt1 = []
for i in range(5):
    kt = input()
    ak = len(kt)
    if i==0 :
        for j in range(0, ak, 4):
            dt1.append(kt[j:j + 3])
    else :
        k = 0
        for j in range(0, ak, 4):
            dt1[k] += kt[j:j + 3]
            k += 1
hls = ""
hh = True
for i in dt1:
    try:
        hls += data[i]
    except :
        hh = False
if hh :
    if int(hls)/6 == int(int(hls)/6):
        print("BEER!!")
    else :
        print("BOOM!!")
else :
    print("BOOM!!")

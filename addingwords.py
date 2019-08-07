import sys
data = {}
data1 = {}
def main ():
    for kata in sys.stdin :
        dt = kata.split()
        if dt[0] == "clear" :
            data.clear()
            data1.clear()
            continue
        if dt[0] == "def" :
            if dt[1] not in data :
                data[dt[1]] = dt[2]
                data1[dt[2]] = dt[1]
            else :
                del  data1[data[dt[1]]]
                data[dt[1]] = dt[2]
                data1[dt[2]] = dt[1]
        elif dt[0] == "calc" :
            bil = ''
            hls = True
            for i in range(1,len(dt)):
                if i % 2 == 1 :
                    if dt[i] in data :
                        bil += data[dt[i]]
                    else :
                        hls = False
                        break
                else :
                    if dt[i] != "=" :
                        bil += dt[i]
            if hls :
                print(" ".join(dt[1:]),end=" ")
                hl = str(eval(bil))
                if hl in data1 :
                    print(data1[hl])
                else :
                    print("unknown")
            else :
                print(" ".join(dt[1:]),"unknown")

main()

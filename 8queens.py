
def main ():
    hls = True
    data = []
    data1 = []
    data2 = []
    for i in range(8):
        dt = list(input())
        if hls :
            for j in range(8) :
                if dt[j] == "*" :
                    if i in data1 :
                        hls = False
                        break
                    if j in data2:
                        hls = False
                        break
                    data1.append(i)
                    data2.append(j)
                    data.append([i,j])
    byk = len(data)
    if byk != 8 :
        hls = False
    if hls :
        for i in range(byk-1) :
            for j in range(i+1,byk):
                if abs(data[i][0] - data[j][0]) == abs(data[i][1] - data[j][1]) :
                    hls = False
                    break
            if hls == False :
                break
    print("valid" if hls else "invalid")

main()

data =[]
byk_dt=[]
for i in range(int(input())):
    kt = input()
    if kt not in data :
        data.append(kt)
        byk_dt.append(1)
    else :
        byk_dt[data.index(kt)] += 1
ak = min(byk_dt)
hls = []
for i in range(len(byk_dt)):
    if byk_dt[i] == ak :
        hls.append(data[i])
hls.sort()
for i in hls :
    print(i)

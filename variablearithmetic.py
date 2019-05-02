data =  {}
while True :
    kt = input()
    if kt == '0' :
        break
    dt = kt.split()
    if '=' in kt :
        data[dt[0]]= dt[2]
        continue
    hls = 0
    dts = []
    for i in dt :
        if i.isnumeric():
            hls += int(i)
        elif i != '+' :
           dts.append(i)
    for i in dts :
        if i in data :
            hls += int(data[i])
    hls1 = ''
    for i in dts :
        if i not in data :
            hls1 += ' + '+i
    if hls==0 :
        print(hls1[3:len(hls1)])
    else  :
        print(str(hls)+hls1)

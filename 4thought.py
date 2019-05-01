byk = int(input())
hls1=[]
for o in range(byk):
    ak = int(input())
    data = ['*','+','-','/']
    hl = 0
    hls =""
    for i in range(4):
        for j in range(4):
            for k in range(4):
                hs = '4 '+data[i]+' 4 '+data[j]+' 4 '+data[k]+' 4 '
                if round(eval(hs))==ak:
                    hl = 1
                    hls = hs
                    break
            if hl == 1 :
                break
        if hl == 1:
            break
    if hl == 0 :
        hls1.append("no solution")
    else :
        hls1.append(hls+'= '+str(ak))
for i in hls1 :
    print(i)


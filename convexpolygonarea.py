for i in range(int(input())):
    data = [int(x) for x in input().split()]
    dtx = []
    dty = []
    byk = data.pop(0)
    for j in range(byk*2):
        if j%2 == 1 :
            dty.append(data[j])
        else :
            dtx.append(data[j])
    rms1 = dtx[byk-1]*dty[0]
    rms2 = dty[byk-1]*dtx[0]
    for j in range(byk-1):
        rms1 += dtx[j]*dty[j+1]
        rms2 += dty[j] * dtx[j + 1]
    print((rms1-rms2)*0.5)

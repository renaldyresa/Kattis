data = []
byk = 0
for i in range(5):
    aa = input()
    for j in range(5):
        if aa [j] == 'k' :
            byk += 1
    data.append(aa)
if byk != 9 :
    print("invalid")
else :
    hl = True
    for i in range(5) :
        for j in range(5):
            if data[i][j] == 'k' :
                if i>=2 and ((j>=1 and data[i-2][j-1]== 'k') or (j<=3 and data[i-2][j+1]== 'k') ) :
                    hl = False
                    break
                if i<=2 and ((j>=1 and data[i+2][j-1]== 'k') or (j<=3 and data[i+2][j+1]== 'k') ):
                    hl = False
                    break
                if j>=2 and ((i>=1 and data[i-1][j-2]== 'k') or (i<=3 and data[i+1][j-2]== 'k' )) :
                    hl = False
                    break
                if j<=2 and ((i>=1 and data[i-1][j+2]== 'k') or (i<=3 and data[i+1][j+2]== 'k' )) :
                    hl = False
                    break
        if hl == False :
            break
    if hl :
        print("valid")
    else :
        print("invalid")


def main ():
    for i in range(int(input())):
        dt = list(map(int,input().split()))
        k = dt.pop(0)
        i,j,byk = 19,19,0
        while True :
            if j == 1 :
                break
            if i == 0 :
                j-=1
                i = j
            if dt[j] < dt[i-1] :
                dt[j],dt[i-1] = dt[i-1],dt[j]
                byk += 1
            else :
                i -= 1
        print(k,byk)

main()

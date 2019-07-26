
def main ():
    data = ['a','i','u','e','o','y']
    while True :
        try :
            kt = list(map(str,input().split()))
            for i in kt :
                dt = list(i)
                for j in range(len(dt)) :
                    if dt[0] not in data :
                        aa = dt.pop(0)
                        dt.append(aa)
                    else :
                        if j== 0 :
                            dt += ['y','a','y']
                        else :
                            dt += ['a','y']
                        break
                print("".join(dt),end=" ")
            print()
        except EOFError :
            break

main()

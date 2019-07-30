def main ():
    data = {}
    i = 1
    while True :
        try :
            kt = input()
            if kt == "OPEN" :
                continue
            if kt == "CLOSE" :
                print("Day",i)
                for key in sorted(data.keys()):
                    print(key+' $'+"{:.2f}".format(sum(data[key])*0.10))
                data = {}
                i+=1
                continue
            dt = kt.split()
            if dt[0]=="ENTER" :
                if dt[1] in data :
                    data[dt[1]] += [int(dt[2])]
                else :
                    data[dt[1]] = [int(dt[2])]
            if dt[0] == "EXIT" :
                masuk = data[dt[1]][-1]
                data[dt[1]][-1] = int(dt[2])- masuk
        except EOFError :
            break
main()

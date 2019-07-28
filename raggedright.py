def main ():
    data = []
    panjang = 0
    while True :
        try :
            kt = input()
            pan = len(kt)
            if panjang < pan :
                panjang = pan
            data.append(pan)
        except EOFError :
            total = 0
            for i in range(len(data)-1):
                total += (panjang-data[i])**2
            print(total)
            break

main()

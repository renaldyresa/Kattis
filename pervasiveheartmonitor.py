while True :
    try :
        data = [x for x in input().split()]
        nama = ''
        jml = 0
        byk = 0
        for i in data :
            if i.isalpha() :
                nama += i+' '
            else :
                byk +=1
                jml += float(i)
        print(jml/byk, nama)
    except EOFError :
        break

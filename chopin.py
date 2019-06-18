i = 1
data = ['A' , 'B', 'C', 'D', 'E' , 'F', 'G']
while True :
    try :
        kt1 , kt2 = map(str,input().split())
        if len(kt1) != 1 :
            if kt1[-1] == '#' :
                if kt1[0] == 'G' :
                    b = 'A'
                else :
                    b = data[data.index(kt1[0])+1]
                b += 'b'
            else :
                b = data[data.index(kt1[0]) - 1]
                b += '#'
            print("Case "+str(i)+": "+b+" "+kt2)
        else :
            print("Case "+str(i)+":"+" UNIQUE")
        i += 1
    except EOFError :
        break

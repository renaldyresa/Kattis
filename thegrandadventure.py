for i in range(int(input())) :
    data = input()
    stack = []
    data = data.replace(".","")
    hls = True
    for j in range(len(data)) :
        hur = data[j]
        if hur == "$" or hur=="|" or hur == "*" :
            stack.insert(0,hur)
        else :
            if len(stack) != 0 :
                if hur == "b" :
                    hur = "$"
                elif hur == "t" :
                    hur = "|"
                else :
                    hur = "*"
                if hur != stack.pop(0) :
                    hls = False
                    break
            else :
                hls = False
                break
    if len(stack)!= 0 :
        hls = False
    print("YES" if hls else "NO")

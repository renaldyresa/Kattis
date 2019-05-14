while True :
    try:
        data = list(map(int,input().split()))
        data.sort(reverse=True)
        hls = 0
        hh = 0
        for i in data :
            hls += i
        for i in data :
            if hls-i == i:
                hh = i
                break
        print(hh)
    except EOFError :
        break

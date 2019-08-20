while True :
    try:
        ak = int(input())
        if ak == 1 :
            print(1)
        else :
            print((ak-1)*2)
    except EOFError :
        break

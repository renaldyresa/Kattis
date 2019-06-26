byk = 1
while True :
    try :
        b,m = map(int,input().split())
        aa = b
        while b%365 != m%687 :
            b += 1
            m += 1
        print("Case "+str(byk)+":",b - aa)
        byk += 1
    except EOFError :
        break

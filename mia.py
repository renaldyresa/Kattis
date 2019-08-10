while True :
    r1,r2,t1,t2 = map(int,input().split())
    if r1 ==0 and r2 == 0 and t1== 0 and t2== 0 :
        break
    if r1<r2 :
        r1,r2 = r2,r1
    if t1<t2 :
        t1,t2 = t2,t1
    hls1 = False
    hls2 = False
    if r1==2 and r2 == 1 :
        hls1 = True
    if t1==2 and t2==1 :
        hls2 = True
    if hls1 or hls2 :
        if hls1 and hls2 :
            print("Tie.")
        elif hls1 :
            print("Player 1 wins.")
        else :
            print("Player 2 wins.")
        continue
    if r1 == r2:
        hls1 = True
    if t1 == t2:
        hls2 = True
    if hls1 or hls2 :
        if hls1 and hls2 :
            if r1==t1:
                print("Tie.")
            elif r1>t1 :
                print("Player 1 wins.")
            else :
                print("Player 2 wins.")
        elif hls1:
            print("Player 1 wins.")
        else:
            print("Player 2 wins.")
        continue
    if r1>t1 :
        print("Player 1 wins.")
    elif r1<t1 :
        print("Player 2 wins.")
    else :
        if r2 > t2 :
            print("Player 1 wins.")
        elif r2 < t2 :
            print("Player 2 wins.")
        else :
            print("Tie.")

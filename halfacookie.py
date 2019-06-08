import math
while True :
    try :
        r,x,y = map (float,input().split())
        titik_p = (x*x+y*y)**(1/2)
        if titik_p >= r :
            print("miss")
        else :
            h = r-titik_p
            potong_a = r*r * math.acos((r-h)/r)-(r-h)*(2*r*h - h*h)**(1/2)
            luas_l = r*r*3.1415926535897
            potong_b = luas_l - potong_a
            hls1 = min(potong_a,potong_b)
            hls2 = max(potong_a,potong_b)
            print(hls2,hls1)
    except EOFError :
        break

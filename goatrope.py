x,y,x1,y1,x2,y2 = map(float,input().split())
if x1<= x and x <=x2 :
    if y1> y :
        print(y1-y)
    else :
        print(y-y2)
elif y1<= y and y <=y2 :
    if x1> x :
        print(x1-x)
    else :
        print(x-x2)
else :
    hx = 0
    hy = 0
    if abs(x-x1) < abs(x-x2) :
        hx = x1
    else :
        hx = x2
    if abs(y - y1) < abs(y - y2) :
        hy = y1
    else :
        hy = y2
    print(((x-hx)**2 + (y-hy)**2)**0.5 )

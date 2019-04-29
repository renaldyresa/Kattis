a,b,c,d = map(int,input().split())
p,m,g = map(int,input().split())
dog1 = a+b
dog2 =  c+d
hp = 0
if p%dog1!=0 and p%dog1<=a :
    hp += 1
if p%dog2!=0 and p%dog2<=c :
    hp += 1
if hp == 2 :
    print("both")
elif hp == 1 :
    print("one")
else :
    print("none")
hp = 0
if m%dog1!=0 and m%dog1<=a :
    hp += 1
if m%dog2!=0 and m%dog2<=c :
    hp += 1
if hp == 2 :
    print("both")
elif hp == 1 :
    print("one")
else :
    print("none")
hp = 0
if g%dog1!=0 and g%dog1<=a :
    hp += 1
if g%dog2!=0 and g%dog2<=c :
    hp += 1
if hp == 2 :
    print("both")
elif hp == 1 :
    print("one")
else :
    print("none")


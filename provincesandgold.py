g,s,c = map(int,input().split())
uang = g*3 + s*2 + c
if uang >= 8 :
    print("Province or",end=' ')
elif uang >= 5 :
    print("Duchy or",end=' ')
elif uang >= 2 :
    print("Estate or",end=' ')
if uang >= 6 :
    print("Gold")
elif uang >=3 :
    print("Silver")
elif uang >=0 :
    print("Copper")

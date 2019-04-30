b,b1,b2,a,a2 = map(int,input().split())
bhls = (b1-b)*b2
a1 = 1
ahls = 0
while bhls >= ahls :
    ahls = a1*a2
    a1 +=1
print(a1-1+a)

ak = int(input())
print(str(ak)+":")
for i in range (2,ak):
    if (ak%(2*i-1)==0)or(ak%(2*i-1)==i):
        print(str(i)+","+str(i-1))
    if (ak%i==0):
        print(str(i)+","+str(i))

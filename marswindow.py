import math
tahun = int(input())
data = []
ak = int(math.ceil((tahun-2017)/2))
hh= 2016
for i in range(ak) :
    hh += 3 if i%6==5 else 2
    data.append(hh)
print("yes" if tahun in data else "no")

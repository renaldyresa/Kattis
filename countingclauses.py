m , n = map(int,input().split())
data = []
for i in range(m) :
    dt= input()
    if dt not in data :
        data.append(dt)
if len(data) < 8 :
    print("unsatisfactory")
else :
    print("satisfactory")

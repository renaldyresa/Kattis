data = []
while True :
    try :
        dt = list(map(str,input().split()))
        data = data+dt
    except EOFError :
        break

data.sort()
hls = []
for i in range (len(data)):
    for j in range(len(data)):
        if i != j :
            kt = data[i]+data[j]
            if kt not in hls :
                hls.append(kt)
hls.sort()
for i in hls:
    print(i)


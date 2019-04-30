data =  list(map(int,input().split()))
data.sort()
if data[2]-data[1]==data[1]-data[0]:
    print(data[2]+abs(data[1]-data[0]))
elif data[2]-data[1] > data[1]-data[0]:
    print(data[1]+abs(data[1]-data[0]))
else :
    print(data[0]+abs(data[2]-data[1]))

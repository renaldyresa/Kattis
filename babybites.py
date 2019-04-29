byk = int(input())
data = list(map(str,input().split()))
j = 1
hls = 0
for i in data :
    if i == str(j) :
        j+=1
    elif i == "mumble" :
        j +=1
    else :
        hls = 1
        break
if hls == 0 :
    print("makes sense")
else :
    print("something is fishy")

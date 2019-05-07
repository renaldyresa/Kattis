n,m = map(int,input().split())
limit = n
hls = 0
for i in range(m):
    kt1,ak = map(str,input().split())
    kt2 = int(ak)
    if kt1 == "enter" :
        if limit-kt2 >= 0 :
            limit = limit-kt2
        else :
            hls += 1
    elif kt1 == "leave":
        limit += kt2
print(hls)

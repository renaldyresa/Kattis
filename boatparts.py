p,n = map(int,input().split())
data = []
out = False
for i in range(n):
    item = input()
    if item not in data :
        data.append(item)
        if len(data)==p :
            hls = i+1
            out = True
if out :
    print(hls)
else :
    print("paradox avoided")

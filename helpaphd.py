byk = int(input())
for i in range (byk):
    data = input()
    if data == "P=NP" :
        print("skipped")
    else :
        n,m = map(int,data.split("+"))
        hls = n+m
        print(hls)

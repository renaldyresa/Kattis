pl = int(input())
ques = int(input())
time = 210
hls = True
for i in range(ques):
    n , m  = map(str,input().split())
    time -= int(n)
    if time<0 :
        hls = False
    if hls :
        if m=='T':
            pl+=1
            if pl==9 :
                pl=1
print(pl)

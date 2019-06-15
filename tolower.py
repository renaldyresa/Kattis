p , t = map(int , input().split())
hls = 0
for i in range(p):
    hh = True
    for j in range(t):
        kt = input()
        if kt[1:].islower() == False:
            hh = False
    if hh :
        hls += 1
print(hls)

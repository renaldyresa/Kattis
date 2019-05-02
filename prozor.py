r,s,p = map(int,input().split())
data=[]
for i in range(r):
    data.append(list(input()))
best = 0
haw1 = 0
haw2 = 0
for i in range(0, s-p + 1):
    for j in range(0, r-p + 1):
        tot = 0
        for x in range(i + 1, i + p - 1):
            for y in range(j + 1, j + p - 1):
                 if data[y][x] == '*':
                    tot += 1
        if tot > best:
            haw1 = j
            haw2 = i
            best = tot
print(best)
for i in range(r):
    for j in range(s):
        if (haw1==i and haw2==j)or(haw1+p-1==i and haw2+p-1==j)or ((haw1==i and haw2+p-1==j))or (haw1+p-1==i and haw2==j):
            print("+",end="")
        elif (haw1 < i and i==haw1+p-1)and(haw2<j and j<haw2+p-1):
            print("-",end="")
        elif (i== haw1 )and(haw2<j and j<haw2+p-1):
            print("-",end="")
        elif (haw1<i and i<haw1+p-1)and(j==haw2):
            print("|",end="")
        elif (haw1<i and i<haw1+p-1)and(j==haw2+p-1):
            print("|",end="")
        else :
            print(data[i][j],end="")
    print()

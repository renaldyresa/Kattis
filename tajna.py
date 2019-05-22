kt = input()
ak = len(kt)
i,j =ak,1
while True :
    if i<=j and i*j==ak:
        break
    j += 1
    i = int(ak/j)
data=[]
p = 0
for k in range(j):
    dt = []
    for l in range(i):
        dt.append(kt[p])
        p+=1
    data.append(dt)
for k in range(i):
    for l in range(j):
        print(data[l][k],end='')

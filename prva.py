n,m = map(int,input().split())
data = []
data1 = data.copy()
for i in range(n):
    kt = input()
    data.append(kt)
    aa = list(map(str, kt.split("#")))
    for k in aa:
        if len(k) >= 2:
            data1.append(k)
for i in  range(m):
    kt = ''
    for j in range(n):
        kt+=data[j][i]
    aa = list(map(str,kt.split("#")))
    for k in aa :
        if len(k)>=2 :
            data1.append(k)
data1.sort();
print(data1[0])

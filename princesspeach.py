ak1,ak2 = map(int,input().split())
data = []
for  i in range(ak2):
    aa = int(input())
    if aa not in data :
        data.append(aa)
for i in range(ak1):
    if i not in data :
        print(i)
print("Mario got",len(data),"of the dangerous obstacles.")

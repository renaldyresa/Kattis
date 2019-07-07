baris , kolom = map(int,input().split())
data = []
for i in range(baris):
    data.append(input())
hls = 1
for i in range(kolom):
    hl = True
    for j in range(baris):
         if data[j][i] == "$" :
             hl = False
             break
    if hl :
        hls +=1
print(hls)

hf = ord("A")
data = []
for i in range(4):
    for j in range(4):
        data += [chr(hf)]
        hf += 1
hls = 0
for i in range(4):
    dt = list(input())
    for j in range(4):
        if dt[j] != "." :
            ak = data.index(dt[j])
            if  ak != 4*i+j :
                baris = 0
                while ak>=4 :
                    ak -= 4
                    baris += 1
                hls += abs(i-baris)+abs(ak-j)
print(hls)


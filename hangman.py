kata = input()
data = input()
hls1 = []
salah = 10
hls =  0
for i in range(len(kata)):
    if kata[i] not in hls1 :
        hls1.append(kata[i])
for i in range(len(data)):
    if len(hls1) == 0 :
        hls = 1
        break
    if data[i] in hls1 :
        hls1.remove(data[i])
    else :
        salah -=1
    if salah == 0 :
        break
if hls == 1 :
    print("WIN")
else :
    print("LOSE")

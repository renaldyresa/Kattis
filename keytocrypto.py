data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cip = input()
key = input()
hls = ""
j = 0
k = 0
for i in range(len(cip)):
    if len(key)>i :
        ak1 = data.index(cip[i])-data.index(key[j])
        hls += data[ak1%26]
        j += 1
    else :
        ak1 = data.index(cip[i])-data.index(hls[k])
        hls += data[ak1%26]
        k += 1
print(hls)

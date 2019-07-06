kata = input()
data = list(kata)
hls = []
for i in data :
    if i not in hls :
        hls.append(i)
    else :
        hls.remove(i)
print(len(hls)-1 if len(hls)>0 else 0)

data = list(map(str,input().split()))
hls = 0
for i in range(len(data)):
    if "ae" in data[i] :
        hls += 1
hh = hls/len(data)*100
if hh >= 40 :
    print("dae ae ju traeligt va")
else :
    print("haer talar vi rikssvenska")

data1 = ['th','in','ft','yd','ch','fur','mi','lea','thou','inch','foot','yard','chain','furlong','mile','league']
data2 = [1,1000,12,3,22,10,8,3]
kt = list(map(str,input().split()))
ak1 = data1.index(kt[1])%8
ak2 = data1.index(kt[3])%8
hls = int(kt[0])
if ak1 > ak2 :
    for i in range(ak1,ak2,-1) :
        hls *= data2[i]
else :
    for i in range(ak1+1,ak2+1,1):
        hls /= data2[i]
print(hls)

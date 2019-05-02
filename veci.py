from itertools import permutations
ak =  input()
data = list(ak)
data.sort(reverse=True)
perm = permutations(data)
hlss = "".join(data)
for i in perm :
    hls = "".join(i)
    if ak < hls :
        if hls < hlss :
            hlss = hls
if ak == hlss :
    print("0")
else :
    print(hlss)

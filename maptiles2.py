data = input()
byk = len(data)
hls = 0
hls1 = 0
for i in range(byk):
    hls1 += int(data[i])%2*(2**(byk-i-1))
for i in range(byk):
    if int(data[i]) >= 2 :
       hls += int(2**(byk-i)/2)
print(byk,hls1,hls)

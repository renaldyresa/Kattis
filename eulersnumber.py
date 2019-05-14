angka = int(input())
hls = 1
an = 1
for i in range(1,angka+1):
    an = an*i
    hls += 1/an
print(hls)

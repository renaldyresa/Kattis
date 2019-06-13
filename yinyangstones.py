data = input()
b_putih = 0
b_hitam = 0
for i in range(len(data)):
    if data[i] == 'W' :
        b_putih +=1
    else :
        b_hitam +=1
print(1 if b_hitam==b_putih else 0)

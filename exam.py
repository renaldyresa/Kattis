t_benar = int(input())
j_sy = input()
j_tmn = input()
sama = 0
beda = 0
for i in range(len(j_sy)):
    if j_sy[i]==j_tmn[i]:
        sama+=1
    else :
        beda+=1
if sama>=t_benar:
    print(t_benar+beda)
else :
    print(sama+(beda-(t_benar-sama)))

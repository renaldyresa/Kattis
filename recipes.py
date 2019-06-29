for i in range(1,int(input())+1):
    n_bahan = []
    p_bahan = []
    b_utama = 0
    bykb, res,diin = map(int,input().split())
    for j in range(bykb):
        nama, berat , persen = map(str,input().split())
        if float(persen) == 100.0 :
            b_utama = float(berat)
        n_bahan.append(nama)
        p_bahan.append(float(persen))
    skala = b_utama*(diin/res)
    print("Recipe #",i)
    for j in range(bykb):
        print(n_bahan[j],'{:.1f}'.format(skala*p_bahan[j]/100))
    print("-"*40)

ak1, ak2 = map(int, input().split())
if ak1 <= ak2 :
    for i in range(ak1+1,ak2+2):
        print(i)
if ak1 > ak2 :
    for i in range(ak2+1,ak1+2):
        print(i)

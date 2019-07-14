data = {}
byk_data, case = map(int, input().split())
for i in range(byk_data):
    nama , nilai = map(str,input().split())
    data[nama] = int(nilai)
for i in range(case) :
    total = 0
    while True :
        kt = input()
        if kt == "." :
            break
        for j in kt.split():
            if j in data :
                total += data[j]
    print(total)

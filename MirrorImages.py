byk = int(input())
for i in range(byk):
    a,b = map(int, input().split(" "))
    data= []
    for j in range(a):
            data.append(input())
    print("Test ",(i+1))
    for j in range(a-1,-1,-1):
        for k in range(b-1,-1,-1):
            print(data[j][k],end="") 
        print("")

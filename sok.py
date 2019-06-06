data1 = [int(x) for x in input().split()]
data2 = [int(x) for x in input().split()]
minimum = min(data1[i]/data2[i] for i in range(3))
for i in range(3):
    print(data1[i]-data2[i]*minimum,end=" ")

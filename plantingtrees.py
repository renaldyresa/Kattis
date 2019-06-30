bibit = int(input())
hari = [int(x) for x in input().split()]
hari.sort(reverse=True)
t_hari = 0
for i in range(bibit):
    t_hari = max(t_hari,hari[i]+i)
print(t_hari+2)

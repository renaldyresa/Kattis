byk = int(input())
data = list(map(int,input().split()))
data.sort(reverse=True)
alice = 0
bob = 0
for i in range(len(data)) :
    if i%2==0:
        alice += data[i]
    else :
        bob += data[i]
print(alice,bob)

ak = int(input())
data1 = input()
data2 = input()
for i in range(ak):
    data1 = data1.replace("0","-")
    data1 = data1.replace("1","0")
    data1 = data1.replace("-","1")
if data2 == data1 :
    print("Deletion succeeded")
else :
    print("Deletion failed")

byk = int(input())
data =[]
for i in range (byk):
    kt = input()
    a,b= kt.split(" ")
    if a == "entry" :
        if b not in data :
            data.append(b)
            print (b,"entered")
        else :
            print (b,"entered (ANOMALY)")
    elif a == "exit" :
        if b in data :
            data.remove(b)
            print (b,"exited")
        else :
            print (b,"exited (ANOMALY)")

while True :
    data = input()
    if data == "0" :
        break
    dt = list(map(float, data.split()))
    print(((abs(dt[0]-dt[2]))**dt[4]+(abs(dt[1]-dt[3]))**dt[4])**(1/dt[4]))

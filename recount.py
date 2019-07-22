def main ():
    data = {}
    while True :
        inp = input()
        if inp == "***" :
            break
        if inp not in data :
            data[inp] = 1
        else :
            data[inp] += 1
    ll = [x for x in data.values()]
    print("Runoff!" if ll.count(max(ll)) > 1 else max(data, key=data.get))

main()

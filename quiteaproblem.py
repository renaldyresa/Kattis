while True :
    try :
        data = input().lower()
        if "problem" in data :
            print("yes")
        else:
            print("no")
    except EOFError :
        break

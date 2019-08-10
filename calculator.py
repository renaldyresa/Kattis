while True :
    try:
        print("{:.2f}".format(eval(input())))
    except EOFError :
        break

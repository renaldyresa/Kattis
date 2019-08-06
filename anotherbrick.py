def main ():
    h,w,n = map(int,input().split())
    data = list(map(int,input().split()))
    hight ,length = 0,0
    hls = False
    for i in data :
        length += i
        if length == w :
            length = 0
            hight += 1
            if hight == h :
                hls = True
                break
        if length > w :
            break
    print("YES" if hls else "NO")

main()

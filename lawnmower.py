def check(lis , w) :
    for i in range(1,len(lis)):
        if lis[i]-lis[i-1] > w :
            return False
    return True
def main ():
    while True :
        nx, ny, w = map(float,input().split())
        if nx == 0 and ny == 0 and w == 0 :
            break
        dt_nx = [float(x) for x in input().split()]
        dt_ny = [float(x) for x in input().split()]
        hls1,hls2 = False,False
        dt_nx.sort()
        dt_ny.sort()
        if check(dt_nx,w) and dt_nx[0] <= w/2 and dt_nx[-1] >= 75-(w/2) :
            hls1 = True
        if check(dt_ny,w) and dt_ny[0] <= w/2 and dt_ny[-1] >= 100-(w/2) :
            hls2 = True
        print("YES" if hls1 and hls2 else "NO")
main()

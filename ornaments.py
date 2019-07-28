import math
def main ():
    while True :
        r,h,s = map(int,input().split())
        if r==0 and h==0 and s == 0 :
            break
        total = 0
        total  += math.sqrt((math.pow(h,2))-(math.pow(r,2))) * 2
        total += 2*math.pi*((360-2 * math.acos(r/h)*180/math.pi)/360)*r
        total += total*(s/100)
        print("{:0.2f}".format(total))
main()

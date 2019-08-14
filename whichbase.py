
def okt(ak,hls,i):
    if ak%10>7 :
        return 0
    if ak <= 0 :
        return hls
    return okt(int(ak/10),hls+((8**i)*(ak%10)),i+1)

def hek(ak,hls,i):
    if ak <= 0 :
        return hls
    return hek(int(ak/10),hls+((16**i)*(ak%10)),i+1)

for i in range(int(input())):
    no, ak = map(int,input().split())
    print(no,okt(ak,0,0),ak,hek(ak,0,0))

ak = int(input())
data = list(input())
stuck = []
hl = True
hls1,hls2 = '',0
for i in range(ak):
    aa= data[i]
    if aa!=' ':
        if aa==')' or aa==']' or aa=='}':
            if len(stuck)==0 :
                hls1, hls2 = aa, i
                hl = False
                break
            if aa==')':
                if stuck.pop(0) != '(' :
                    hls1,hls2 = aa,i
                    hl = False
                    break
            elif aa==']':
                if stuck.pop(0) != '[' :
                    hls1, hls2 = aa, i
                    hl = False
                    break
            elif aa=='}':
                if stuck.pop(0) != '{' :
                    hls1, hls2 = aa, i
                    hl = False
                    break
        else :
            stuck.insert(0,aa)
print("ok so far" if hl else hls1+" "+str(hls2))

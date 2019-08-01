
def main ():
    data = {'G':[],'F':[],'E':[],'D':[],'C':[],'B':[],'A':[],'g':[],'f':[],'e':[],'d':[],'c':[],'b':[],'a':[]}
    byk = int(input())
    dt = input().split()
    for j in range(byk) :
        kt = dt.pop(0)
        if len(kt)==1 :
            for i in data :
                if i == kt :
                    data[i] += ['*']
                else :
                    data[i]+= ['-'] if (i=='F'or i=='D' or i=='B' or i=='g' or i=='e' or i=='a') else [' ']
                if j!=byk-1 :
                    data[i]+=['-'] if (i=='F'or i=='D' or i=='B' or i=='g' or i=='e' or i=='a') else [' ']
        else :
            hf = kt[0]
            ak = int(kt[1:])
            for i in data :
                if i == hf :
                    data[i] += ['*'*ak]
                else :
                    data[i] += ['-'*ak] if (i=='F'or i=='D' or i=='B' or i=='g' or i=='e' or i=='a') else [' '*ak]
                if j!=byk-1 :
                    data[i]+=['-'] if (i=='F'or i=='D' or i=='B' or i=='g' or i=='e' or i=='a') else [' ']
    for i in data :
        print(i+": "+"".join(data[i]))
main()

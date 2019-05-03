ans = {}
ans[0] = "zero";
ans[1] = "one";
ans[2] = "two";
ans[3] = "three";
ans[4] = "four";
ans[5] = "five";
ans[6] = "six";
ans[7] = "seven";
ans[8] = "eight";
ans[9] = "nine";
ans[10] = "ten";
ans[11] = "eleven";
ans[12] = "twelve";
ans[13] = "thirteen";
ans[14] = "fourteen";
ans[15] = "fifteen";
ans[16] = "sixteen";
ans[17] = "seventeen";
ans[18] = "eighteen";
ans[19] = "nineteen";
ans[20] = "twenty";
ans[30] = "thirty";
ans[40] = "forty";
ans[50] = "fifty";
ans[60] = "sixty";
ans[70] = "seventy";
ans[80] = "eighty";
ans[90] = "ninety";

for j in range(20, 100, 10):
    for i in range(1, 10):
        ans[j+i] = ans[j] + '-' + ans[i];

while True :
    try :
        kt = list(map(str,input().split()))
        j = 0
        for i in kt :
            if i.isnumeric():
                if j==0 :
                    num = ans[int(i)]
                    num1 = num[0].upper()+num[1:]
                    print(num1,end=' ')
                else :
                    num = ans[int(i)]
                    print(num, end=' ')
            else :
                print(i,end=' ')
            j+=1
    except EOFError:
        break

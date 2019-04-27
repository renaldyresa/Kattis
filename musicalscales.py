data = { 0 : ['A','B','C#','D','E','F#','G#'],
         1 : ['A#','C','D','D#','F','G','A'],
         2 : ['B','C#','D#','E','F#','G#','A#'],
         3 : ['C','D','E','F','G','A','B'],
         4 : ['C#','D#','F','F#','G#','A#','C'],
         5 : ['D','E','F#','G','A','B','C#'],
         6 : ['D#','F','G','G#','A#','C','D'],
         7 : ['E','F#','G#','A','B','C#','D#'],
         8 : ['F','G','A','A#','C','D','E'],
         9 : ['F#','G#','A#','B','C#','D#','F'],
         10 : ['G','A','B','C','D','E','F#'],
         11 : ['G#','A#','C','C#','D#','F','G']}
byk = int(input())
inp = list(map(str,input().split()))
hl = []
hls = []
for i in range(byk):
    if inp[i] not in hl :
        hl.append(inp[i])
for i in range(int(12)) :
    k = 0
    for j in range(len(hl)) :
        if hl[j] not in data[i]:
            k = 1
            break
    if k == 0 :
        hls.append(data[i][0])
if len(hls)==0 :
    print('none')
else :
    for i in range(len(hls)):
        print(hls[i],end=' ')

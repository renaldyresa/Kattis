data ={ 'A' : '.-','B' : '-...','C' : '-.-.','D' : '-..','E' : '.',
        'F' : '..-.','G' : '--.','H' : '....','I' : '..','J' : '.---',
        'K' : '-.-','L' : '.-..','M' : '--','N' : '-.','O' : '---',
        'P' : '.--.','Q' : '--.-','R' : '.-.','S' : '...','T' : '-',
        'U' : '..-','V' : '...-','W' : '.--','X' : '-..-','Y' : '-.--',
        'Z' : '--..','_' : '..--',',' : '.-.-','.' : '---.','?' : '----',
       }
while True :
    try:
        cip = input()
        morse = ''
        ak = []
        for i in cip :
            morse+=data[i]
            ak.insert(0,len(data[i]))
        k=0
        i=0
        hls =""
        while i<len(morse):
            for j in data :
                if data[j]==morse[i:(ak[k]+i)]:
                    hls+=j
                    break
            i+=ak[k]
            k+=1
        print(hls)
    except EOFError :
        break

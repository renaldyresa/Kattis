def main ():
    data = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(int(input())):
        teks = input()
        if teks[0] == "e" :
            teks = teks[2:]
            hls = teks[0]
            ak = data.index(teks[0])
            for j in range(1,len(teks)):
                ak += data.index(teks[j])
                hls += data[ak%27]
            print(hls)
        else :
            teks = teks[2:]
            ak = 0
            hls = teks[0]
            dt = [data.index(teks[0])]
            for j in range(1,len(teks)):
                hf = data.index(teks[j])
                if hf < data.index(teks[j-1]):
                    ak += 1
                dt.append((ak*27)+hf)
                hls += data[dt[j]-dt[j-1]]
            print(hls)

main()

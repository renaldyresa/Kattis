biner = input()
while len(biner)%3!=0 :
    biner = "0"+biner
hls = ""
for i in range(0,len(biner),3):
    if biner[i:i+3] == "000" :
        hls+="0"
    elif biner[i:i+3] == "001" :
        hls+="1"
    elif biner[i:i+3] == "010" :
        hls+="2"
    elif biner[i:i+3] == "011" :
        hls+="3"
    elif biner[i:i+3] == "100" :
        hls+="4"
    elif biner[i:i+3] == "101" :
        hls+="5"
    elif biner[i:i + 3] == "110":
        hls += "6"
    elif biner[i:i+3] == "111" :
        hls+="7"
print(int(hls))

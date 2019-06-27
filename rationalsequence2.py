for i in range(int(input())):
    ak,dt = map(str,input().split())
    data1 = int(dt.split("/")[0])
    data2 = int(dt.split("/")[1])
    string = ""
    while data1 != data2 :
        if data1 > data2 :
            string += "R"
            data1 -= data2
        else :
            string += "L"
            data2 -= data1
    index = len(string)-1
    hls = 0
    while index != -1 :
        if string[index]=="R" :
            hls = 2*(hls+1)
        else :
            hls = 2*hls+1
        index -= 1
    print(ak,hls+1)

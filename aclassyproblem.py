def getRank(name, strRank: str):
    return f'{(strRank.replace("upper", "a").replace("middle", "b").replace("lower", "c").replace("-", "")[::-1] + ("b"*10))[:10]}{name[:-1]}'    

def main():
    totalCase = int(input())
    for i in range(totalCase):
        totalPeople = int(input())
        classies = []
        for j in range(totalPeople):
            name, rank, _ = list(map(str, input().split()))
            classies.append(getRank(name=name, strRank=rank))
        for classy in sorted(classies):
            print(classy[10:])
        print("==============================")


if __name__ == "__main__":
    main()

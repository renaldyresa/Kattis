
class Company:

    def __init__(self):
        self.__companies = []

    def setCompany(self, companies: list):
        self.__companies = companies

    def updateLocation(self, com: int, location: int):
        self.__companies[com-1] = location

    def getDistance(self, comA: int, comB: int) -> int:
        return abs(self.__companies[comA-1] - self.__companies[comB-1])


def main():
    totalCompany, totalQuery = list(map(int, input().split()))
    company = Company()
    company.setCompany(list(map(int, input().split())))
    for _ in range(totalQuery):
        noQ, a, b = list(map(int, input().split()))
        if noQ == 1:
            company.updateLocation(a, b)
        else:
            print(company.getDistance(a, b))


if __name__ == "__main__":
    main()

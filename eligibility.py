byk = int(input())
for i in range (byk):
    name,study,born,course = map(str,input().split())
    if int(study.split('/')[0])>=2010 or int(born.split('/')[0])>=1991:
        print(name+" eligible")
    elif int(course)>40 :
        print(name+ " ineligible")
    else :
        print(name+" coach petitions")

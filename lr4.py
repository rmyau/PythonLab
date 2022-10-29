#дана информация о цветных кубиках у двух детей.
#найти количество цветов, которые есть хотя бы у одного ребенка и
#кол-во цветов, которые есть у обоих

a1={'желтый', 'синий','зеленый'}
a2={'синий','фиолетовый','зеленый','красный'}

AorB=a1.union(a2)
print('Количество цветов, которые есть хотя бы у одного ребенка: ', len(AorB))
for color in AorB:
    print(color)

AandB = a1&a2
print('Количество цветов, которые есть у обоих: ', len(AandB))
for color in AandB:
    print(color)


#дано количество учеников, для каждого из учеников даны языки, которые он знает
#найти языки коорые знает хотя бы один, найти которые знают все
def stripFunc(a):
    return a.strip()
def second():
    n=int(input("Введите количество учеников: "))
    print("Input: ")
    stud=list(map(stripFunc,input().split(',')))
    studDiz = set(stud)
    studCon = set(stud)
    for i in range(n-1):
        stud=set(map(stripFunc,input().split(',')))
        studDiz|=stud
        studCon&=stud
    print('Языки, которые знает хотя бы один: ')
    for lang in studDiz:
        print(lang)
    print('Языки, которые знают все: ')
    for lang in studCon:
        print(lang)

    print('''русский, английский
    русский, итальяснкий
    русский, английский, испанский''')
#дано кол-во дней, кол-во политических партий. Для каждой партии известен
#первый день забастовки и период с которым забастовка повторяется
#день забастовки считается нерабочим днем.
#в первый день всегда понедельникб сб и вс - выходные.
#сколько было рабочих дней
days = int(input('Введите количество дней: '))
party = int(input('Введите количество партий: '))
def delWeek(a):
    if a%7==0 or a%7==6:
        return 0
    else: return a
work=set(map(delWeek,range(1,days+1)))-{0}
print('Введите данные о забастовках: ')
for i in range(party):
    info = list(map(int,input().split()))
    while info[0]<days:
        work-=set(info[0])
        info[0]+=info[1]
        
        








    


def first():
    for i in range(10,100):
        if (i//10)*(i%10)*2 == i:
            print(i)

def second():
    for i in range(100,1000):
        if (i**2)%1000 == i:
            print(i)

def third():
    n= int(input("Введите n: "))
    for i in range(100,1000):
        if (i//100) + (i//10%10)+(i%10) == n:
            print(i)

def fourth():
    a= int(input("Введите a: "))
    b= int(input("Введите b: "))
    for i in range(a,b+1):
        if i>999 and i<10000:
            s1 = str(i)
            s2=str(i)[::-1]
            if s1==s2:
                print(i)
def fifth():
    a= int(input("Введите a: "))
    b= int(input("Введите b: "))
    for i in range(a,b+1):
        if i>999 and i<10000:
            s1=str(i)
            if s1.count(s1[3])==3 or s1.count(s1[0])==3:
                print(i)


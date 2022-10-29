#найти макс кол-во идущих подряд равных элементов

def f1():
    a=[]
    a= list(map(int, input("Введите массив: ").split()))
    elM=a[0]
    km = 1
    k=1
    for i in range(1,len(a)+1):
        if i==len(a):
            if k>km:
                km=k
                elM=a[i-1]
        else:
            if a[i] ==a[i-1]:
                k+=1
            elif k>km:
                km=k
                elM=a[i-1]
                k=1
    
    print(elM, km)
#макс длину монотонного фрагмента
def f2():
    a=[]
    a= list(map(int, input("Введите массив: ").split()))
    kmUp=1
    kmDown=1
    kUp=1
    kDown=1
    for i in range(1,len(a)):
        if a[i]>=a[i-1]:
            kUp+=1
        elif kUp>kmUp:
            kmUp=kUp
            kUp=1
        if a[i]<=a[i-1]:
            kDown+=1
        elif kDown>kmDown:
            kmDown = kDown
            kDown=1
    if kmDown>kmUp:
        print(kmDown)
    else:
        print(kmUp)

#найти количество локальных максимумов
def f3():
    a=[]
    a= list(map(int, input("Введите массив: ").split()))
    k=0
    for i in range(1,len(a)-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            k+=1
    print(k)

#найти минимальное расстояние между локальными максимумами
def f4():
    
    a=[]
    a= list(map(int, input("Введите массив: ").split()))
    rMin=-1
    indMax=-1
    for i in range(1,len(a)-1):
        if a[i]>a[i-1] and a[i]>a[i+1]:
            if indMax==-1:
                print(str(i)+"=indMax")
                indMax=i
            elif i-indMax<rMin or rMin==-1:
                rMin=i-indMax

    print(rMin)
f4()
        
            
            
    
        

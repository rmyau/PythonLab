def f1():
    n=int(input("Введите количество пар: "))
    d={}
    print("введите:")
    for i in range(n):
        k=list(input().split(' '))
        d[k[0]] = k[1]
    while True:
        word = input("Синоним для слова: ")
        if word in d:
            print("Синоним: "+d[word])
        else:
            for key in d:
                if d[key]==word:
                    print('Синоним: '+key )
            
    
#Дана строка, для каждого слова определить, сколько раз оно встречалось ранее
def f2():
    s=input('Введите строку: ')
    d={}
    res=[]
    words = s.split(" ")
    for word in words:
        if word in d:
            res.append(d[word])
            d[word]+=1
        else:
            res.append(0)
            d[word]=1
    print(res)

def f3():
    s=input('Введите строку: ')
    d={}
    words = s.split(" ")
    words.sort()
    print(words)
    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    m=0
    for word in d:
        if d[word]>m:
            m=d[word]
            maxWord=word
    print(maxWord)

def f1():
    file= open('Files Python/input1.txt')
    s=file.read().strip().replace('\n',' ')
    s=set(s.split(' '))
    print(len(s))
    file.close()
def f2():
    sumList=[]
    file= open('Files Python/input2.txt')
    for line in file:
        s=list(map(int,line.split()))
        sumLine=0
        for i in s:
            sumLine+=i
        sumList.append(sumLine)
    for summ in sumList:
        print(summ,end=' ')

def invert(s):
    res=''
    for i in s:
        ind= ord(i)-97
        ind=25-ind
        res+=chr(ind)
    return res    
def f3():
    file= open('Files Python/input3.txt')
    out=open('Files Python/output3.txt','w')
    s=file.read().strip()
    s=s.split()
    d={}
    for word in s:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    d_list=sorted(d,key = lambda word: str(d[word])+invert(word),reverse=True)
    for key in d_list:
        out.write(key+'-'+str(d[key])+'\n')
    out.close()
def f4():
    file= open('Files Python/input4.txt')
    out=open('Files Python/output4.txt','w')
    s=file.readlines()[::-1]
    for line in s:
        out.write(line)
    out.close()

def f5():
    file= open('Files Python/input5.txt')
    lineC=0
    words=[]
    for line in file:
        lineC+=1
        words.extend(line.strip().split())
    alf=0
    print(words)
    for word in words:
        for ch in word:
            if word.isalpha():
                alf+=1
    print("alf = ", alf,'\nwords = ',len(words),'\nlines = ', lineC)
    
    
f5()
    

             
    

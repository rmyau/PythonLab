# в строке после точки и запятой один пробел пробелы только одни

def joinStr(s,simb):
    sList=s.split(simb)
    for i in range(len(sList)):
        sList[i]=sList[i].strip()
    print(sList)
    simb+=' '
    s=simb.join(sList)
    return s

def f1():
    s=input()
    s=s.strip()
    #hello ,  world .Nice   day.
    sList=s.split()
    for i in range(len(sList)):
        sList[i]=sList[i].strip()
    s=' '.join(sList)
    s=joinStr(s,'.')
    s=joinStr(s,',')
    print(s)

def f2():
    #Was.it.a.rat.I.saw?
    s=input()
    newS=''
    for simb in s:
        if simb>='A' and simb<='z':
            newS+=simb
    s=newS.lower()
    s2=s[::-1]
    for i in range(len(s)):
        if s[i]!=s2[i]:
            return False
    return True

def f3(k,s):
    if k==1:
        return s
    k-=1
    a=s[0]
    n=0
    newS=''
    for simb in s:
        if simb==a:
            n+=1
        else:
            newS+=str(n)+a
            n=1
            a=simb
    newS+=str(n)+a
    return f3(k,newS)
    
#print(f3(3,'1'))
#нерабочее - сделать удаление с начала
def f4():
    s=input()
    pal=s.copy()
    pal2=pal[::-1]
    
    while pal!=pal2 or pal!='':
        pal=pal[0:-1]
        pal2=pal[::-1]
    print(pal)
            
            
            
        
        
        
        
        
    

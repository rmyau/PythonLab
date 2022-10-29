#игральные кости
import random
d={}
for i in range(2,13):
    d[i]=0
def randomCubeSum():
    a1=random.randint(1,6)
    a2=random.randint(1,6)
    return a1+a2
for i in range(1000):
    s=randomCubeSum()
    d[s]+=1
dOzh={2:2.78,3:5.56,4:8.33,5:11.11,6:13.89,7:16.67,8:13.89,9:11.11,10:8.33,11:5.56,12:2.78}
print("Исход\t  Процент симуляции  Ожидаемый процент")
for key in d:
    print(key, '\t--\t',d[key]/10,"\t--\t",dOzh[key])

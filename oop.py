class Point:
    def __init__(self, x=float(0), y=float(0)):
        self.x=x
        self.y=y


#исключения на ввод
#выпуклость
def Subt(p1,p2):#point
    return Point(p1.x-p2.x,p1.y-p2.y)
def ccw(p1,p2):
    return p1.x*p2.y - p1.y*p2.x
def intersect(v1,v2,v3,v4):#point
    return (((ccw(Subt(v2,v1),Subt(v3,v1))<=0) != (ccw(Subt(v2,v1),Subt(v4,v1))<=0))
            and ((ccw(Subt(v4,v3),Subt(v2,v3))<=0) != (ccw(Subt(v4,v3),Subt(v1,v3))<=0)))

def isIntersect(q,p):
    for edQ in q.edge:
        for edP in p.edge:
            if intersect(edQ[0],edQ[1],edP[0],edP[1]):
                return True
    return False

def isInclude(q,p): #p in q
    newEdge=[]
    cent=q.center
    for v in p.vertex:
        newEdge.append((cent, v))
    for edQ in newEdge:
        for edP in q.edge:
            if intersect(edQ[0],edQ[1],edP[0],edP[1]):
                return False
    return True

def zcross(e1, e2):
    p1 = e1[0]
    p2 = e1[1]
    p3 = e2[1]
    dx1 = p2.x-p1.x
    dy1 = p2.y-p1.y
    dx2 = p3.x-p2.x
    dy2 = p3.y-p2.y
    return dx1*dy2 - dy1*dx2                

class Quad:
    vertex = []
    edge=[]
    def isVipucle(self):
        crosses = []
        for i in range(len(self.edge) - 1):
            
            e1 = self.edge[i]
            e2 = self.edge[i+1]
            crosses.append(zcross(e1, e2))
        crosses.append(zcross(self.edge[len(self.edge) - 1], self.edge[0]))
     
        for i in range(len(crosses) - 1):
            if crosses[i] * crosses[i+1] < 0:
                return False
        if crosses[0] * crosses[len(crosses) - 1] < 0:
            return False
     
        return True
    
    def __init__(self,a=(0,0),b=(1,0),c=(0,1),d=(1,1),id_s=1):
        self.vertex.append(Point(a[0],a[1]))
        self.vertex.append(Point(b[0],b[1]))
        self.vertex.append(Point(c[0],c[1]))
        self.vertex.append(Point(d[0],d[1]))
    
        self.edge.append((self.vertex[0],self.vertex[1]))
        self.edge.append((self.vertex[1],self.vertex[2]))
        self.edge.append((self.vertex[2],self.vertex[3]))
        self.edge.append((self.vertex[3],self.vertex[0]))
        sumX=0
        sumY=0
        for i in range(4):
            sumX += self.vertex[i].x
            sumY +=self.vertex[i].y
        sumX/=4
        sumY/=4
        self.id_s=id_s
        self.center=Point(sumX,sumY)
        if not(self.isVipucle()):
            try:
                raise Exception('фигура не является выпуклой')
            except Exception:
                print("Данная фигура не является выпуклой")
        else:
            print('Квадрат задан корректно')
            
                
        
class Pentagon():
    vertex = []
    edge=[]
    n=5
    def isVipucle(self):
        crosses = []
        for i in range(len(self.edge) - 1):
            
            e1 = self.edge[i]
            e2 = self.edge[i+1]
            crosses.append(zcross(e1, e2))
        crosses.append(zcross(self.edge[len(self.edge) - 1], self.edge[0]))
     
        for i in range(len(crosses) - 1):
            if crosses[i] * crosses[i+1] < 0:
                return False
        if crosses[0] * crosses[len(crosses) - 1] < 0:
            return False
     
        return True
    def __init__(self,a=(0,0),b=(1,0),c=(1,1),d=(0.5,1.2), e=(1,1),id_s=2):
        self.id_s=id_s
        self.vertex.append(Point(a[0],a[1]))
        self.vertex.append(Point(b[0],b[1]))
        self.vertex.append(Point(c[0],c[1]))
        self.vertex.append(Point(d[0],d[1]))
        self.vertex.append(Point(e[0],e[1]))
        
        self.edge.append((self.vertex[0],self.vertex[1]))
        self.edge.append((self.vertex[1],self.vertex[2]))
        self.edge.append((self.vertex[2],self.vertex[3]))
        self.edge.append((self.vertex[3],self.vertex[4]))
        self.edge.append((self.vertex[4],self.vertex[0]))
        
        sumX=0
        sumY=0
        for i in range(5):
            sumX += self.vertex[i].x
            sumY +=self.vertex[i].y
        sumX/=5
        sumY/=5
        self.center=Point(sumX,sumY)
        if not(self.isVipucle()):
            try:
                raise Exception('фигура не является выпуклой')
            except Exception:
                print("Данная фигура не является выпуклой")
        else:
            print('Пятиугольник задан корректно')
try:
    q=Quad(a=(1,1),b=(1,4),c=(4,4),d=(4,1),id_s=2)
    p=Pentagon(a=(2,1.5), b=(1.5,2.5),c=(2,3.5),d=(3,2.5),e=(3,0.5),id_s=3)
    print("Лежит ли пятиугольник внутри квадрата: ",isInclude(q,p))
except TypeError:
    print("gjhgjfhjfdh")



        

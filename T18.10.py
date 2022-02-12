import turtle
import math


class Point2:
    '''Точка екрану

    '''
    def __init__(self, x=None, y=None):
        self._x = x             # _x - координата x точки
        self._y = y             # _y - координата y точки
        self._visible = False   # _visible - чи є точка видимою на екрані
    @property
    def getx(self):
        '''Повертає координату x точки
        '''
        return self._x
    @property
    def gety(self):
        '''Повертає координату y точки
        '''
        return self._y

    def onscreen(self):
        '''Перевіряє, чи є точка видимою на екрані
        '''
        return self._visible

    def switchon(self):
        '''Робить точку видимою на екрані
        '''
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot()

    def switchoff(self):
        '''Робить точку невидимою на екрані
        '''
        if self._visible:
            self._visible = False
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot(turtle.bgcolor())

    def move(self, dx, dy):
        '''Пересуває точку на екрані на dx, dy позицій
        '''
        vis = self._visible
        if vis:
            self.switchoff()
        self._x += dx
        self._y += dy
        if vis:
            self.switchon()


class CompareMixin:
  def __eq__(self,other):
    return not(self<other) and not(other<self)
  def __ne__(self,other):
    return (self<other) or (other<self)
  def __le__(self,other):
    return (self<other)
  def __mo__(self,other):
    return (other<self)
  def __eqle__(self,other):
    return (self<other) or self.__eq__(self,other)
  def __eqmo__(self,other):
    return (other<self) or self.__eq__(self,other)


class XOderPoint2(Point2):
  def __init__(self,x,y):
    super().__init__(x,y)
  def __le__(self,p2):
    return self.getx<p2.getx

class FullXOderPoint2(XOderPoint2, CompareMixin):
    def __init__(self,x,y):
        super().__init__(x,y)
    def __le__(self,other):
        return self.getx<other.getx
    def __eq__(self,other):
        return self.getx==other.getx 
    def __ne__(self,other):
        return self.getx!=other.getx 
    def __mo__(self,other):
        return other.getx<self.getx
    def __eqle__(self,other):
        return self.getx<=other.getx
    def __eqmo__(self,other):
        return other.getx<=self.getx


n=int(input('Input the number of points'))
a=[]
for i in range(n):
    print('Coordinate of {} point'.format(i+1))
    x=float(input('x:'))
    y=float(input('y:'))
    p=FullXOderPoint2(x,y)
    a.append(p)

#сортування методом бульбашки 
for k in range(len(a)):
    for j in range(len(a)-1,k,-1):
        if a[j-1]<=a[j]:
            z=a[j-1]
            a[j-1]=a[j]
            a[j]=z
            
for i in range(len(a)):
    turtle.delay(110)
    a[i].switchon()


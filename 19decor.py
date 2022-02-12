"""
Простий декоратор класу, перевіряє чи аргументи
об'єкту, які є ключами приймають цілий тип даних
"""

def dec(klass):
    old_int = klass.__init__
    old_f=klass.f
    
    def decorated__init__(self, *args ,**kwargs):
        print('@decorator pre ')
        try:
            for t in kwargs.values():    
                if type(t)!=int:
                    raise ValueError
        except ValueError:
            print('Different type than int')                
                
        old_int(self, *args, **kwargs)
        print('@decorator post ')
    def dec_f(self,*args ,**kwargs):
        print("Entrance to the decorator for method  f")
        return old_f(self)
    klass.f=dec_f
    klass.__init__ = decorated__init__
    return klass

@dec
class A:
    def __init__(self,**c):
        self.a=c
    def f(self):
        d={}
        for t in self.a.items():
            print(t)          

d={'qw':5,'u':6}
s=A(**d)
s.f()


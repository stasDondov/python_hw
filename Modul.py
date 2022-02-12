from abc import ABCMeta, abstractmethod
import turtle

class Drawable(metaclass=ABCMeta):
    """Абстрактний клас для зображення точок та кіл заданих розмірів та
   кольору
    """

    @property
    @abstractmethod
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        pass

    @color.setter
    @abstractmethod
    def color(self, cl):
        pass

    @property
    @abstractmethod
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        pass

    @bgcolor.setter
    @abstractmethod
    def bgcolor(self, cl):
        pass

    @abstractmethod
    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        pass

    @abstractmethod
    def draw_circle(self, x, y, r, cl):
        """Зобразити коло з координатами центру x, y радіусом r кольором
       cl."""
        pass

    @abstractmethod
    def draw_cross(self, x1, y1, x2, y2, cl):
        """Зобразимо хрестик з координатами верхнього лівого кута x1, y1
        та координатами лівого нижнього кута x2, y2 кольором cl"""
        pass

    @abstractmethod
    def draw_rectangle(self, x1, y1, x2, y2, cl):
        """Зобразимо прямокутник з координатами верхнього лівого кута x1, y1
        та координатами лівого нижнього кута x2, y2 кольором cl"""
        pass



class TurtleDraw(Drawable):
    """Клас для зображення точок та кіл заданих розмірів та кольору.
    TurtleDraw є нащадком абстрактного класу Drawable та використовує засоби
    роботи з графікою з модуля turtle.
    """

    def __init__(self):
        pause = 50
        turtle.up()
        turtle.home()
        turtle.delay(pause)

    @property
    def color(self):
        """Властивість, що повертає/встановлює колір переднього плану."""
        return turtle.pencolor()

    @color.setter
    def color(self, cl):
        turtle.pencolor(cl)

    @property
    def bgcolor(self):
        """Властивість, що повертає/встановлює колір фону."""
        return turtle.bgcolor()

    @bgcolor.setter
    def bgcolor(self, cl):
        turtle.bgcolor(cl)

    def draw_point(self, x, y, cl):
        """Зобразити точку з координатами x, y кольором cl."""
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.dot(cl)

    def draw_circle(self, x, y, r, cl):
        """Зобразити коло з координатами цeнтру x, y радіусом r кольором
       cl."""
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(x, y - r)  # малює починаючи знизу кола
        turtle.down()
        turtle.circle(r)
        self.color = c

    def draw_cross(self, x1, y1, x2, y2, cl):
        """Зобразимо хрестик з координатами верхнього лівого кута x1, y1
        та координатами лівого нижнього кута x2, y2 кольором cl"""
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(x1, y1)
        turtle.down()
        turtle.setpos(x2, y2)
        turtle.penup()
        turtle.setpos(x2, y1)
        turtle.pendown()
        turtle.setpos(x1, y2)
        turtle.penup()
        self.color = c

    def draw_rectangle(self, x1, y1, x2, y2, cl):
        """Зобразимо прямокутник з координатами верхнього лівого кута x1, y1
        та координатами лівого нижнього кута x2, y2 кольором cl"""
        c = self.color
        self.color = cl
        turtle.up()
        rec_width = x1 - x2
        rec_length = y1 - y2

        turtle.setpos(x1, y1)
        turtle.down()
        turtle.forward(rec_width)
        turtle.right(90)
        turtle.forward(rec_length)
        turtle.right(90)
        turtle.forward(rec_width)
        turtle.right(90)
        turtle.forward(rec_length)
        turtle.penup()
        self.color = c


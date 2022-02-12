import turtle

class CharDraw:
    """Клас для зображення точок, кіл, прямокутників та хрестиків заданих розмірів та кольору.
    CharDraw є нащадком абстрактного класу Drawable та використовує засоби
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
        """Зобразити коло з координатами цнтру x, y радіусом r кольором
        cl."""
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setheading(0)
        turtle.setpos(x + r, y - 2*r)  # малює починаючи знизу кола
        turtle.down()
        turtle.circle(r)
        self.color = c

    def draw_rectangle(self, x, y, height, width, cl):
        """Зобразити прямокутник з координатами верхнього лівого кута x, y,
        висотою height та шириною width кольором cl"""
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.setpos(x + width, y)
        turtle.setpos(x + width, y - height)
        turtle.setpos(x, y - height)
        turtle.setpos(x, y)
        self.color = c

    def draw_cross(self, x, y, height, width, cl):
        """Зобразити хрестик з координатами верхнього лівого кута x, y,
        висотою height та шириною width кольором cl"""
        c = self.color
        self.color = cl
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.setpos(x + width, y - height)
        turtle.penup()
        turtle.setpos(x, y - height)
        turtle.pendown()
        turtle.setpos(x + width, y)
        turtle.setheading(90)
        self.color = c


class Cross_and_Circle(CharDraw):
    def __init__(self):
        CharDraw.__init__(self)
        self.data = {}
        self.width = 90
        self.height = 90

    def draw_field(self):
        count = 0
        for y in (self.height, self.height*(2/3), self.height*(1/3)):
            for x in (0, self.width*(1/3), self.width*(2/3)):
                count += 1
                self.data.update({count: [x, y, 0]})
                self.draw_rectangle(x, y, self.width/3, self.height/3, 'green')

    def play(self):
        turtle.width(3)
        turtle.hideturtle()
        self.draw_field()
        counter = 0
        while counter != 9:
            print()
            pos = int(input('Позиція: '))
            if self.data[pos][2] != 0:
                raise KeyError
            sym = input('Символ: ')

            if sym == 'o':
                self.draw_circle(self.data[pos][0], self.data[pos][1], self.height/6, 'red')
                self.data[pos][2] = -1
            elif sym == 'x':
                self.draw_cross(self.data[pos][0], self.data[pos][1], self.width/3, self.width/3, 'blue')
                self.data[pos][2] = 1

            if (abs(self.data[1][2] + self.data[2][2] + self.data[3][2]) == 3 or
                    abs(self.data[4][2] + self.data[5][2] + self.data[6][2]) == 3 or
                    abs(self.data[7][2] + self.data[8][2] + self.data[9][2]) == 3 or
                    abs(self.data[1][2] + self.data[4][2] + self.data[7][2]) == 3 or
                    abs(self.data[2][2] + self.data[5][2] + self.data[8][2]) == 3 or
                    abs(self.data[3][2] + self.data[6][2] + self.data[9][2]) == 3 or
                    abs(self.data[1][2] + self.data[5][2] + self.data[9][2]) == 3 or
                    abs(self.data[3][2] + self.data[5][2] + self.data[7][2]) == 3):
                print('WIN ' * 100)  # 3 стовпчик
                turtle.penup()
                turtle.setpos(0, 150)
                turtle.write('WIN !!!', font=300)
                break
            counter += 1
        if counter == 9:
            turtle.penup()
            turtle.setpos(0, 150)
            turtle.pendown()
            turtle.write('DRAW', font=300)
                
                
Q = Cross_and_Circle()
Q.play()


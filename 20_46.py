from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *


class Redactor:
    def __init__(self, main):
        self.main = main
        self.main_init()

    def main_init(self):
        self.main.title('Graphics editor')
        self.main.geometry('995x490+400+100')
        self.main.resizable(0, 0)

        Button(self.main,
               text='Draw line', font=17,
               height=6, width=25, background='lightgrey',
               command=self.draw_line).grid(row=0, column=0)

        Button(self.main,
               text='Draw rectangle', font=17,
               height=6, width=25, background='lightgrey',
               command=self.draw_rect).grid(row=1, column=0)

        Button(self.main,
               text='Draw oval', font=17,
               height=6, width=25, background='lightgrey',
               command=self.draw_oval).grid(row=2, column=0)

        Button(self.main,
               text='Exit', font=17,
               width=25, background='lightgrey',
               command=self.exit).grid(row=3, column=3)

        Button(self.main,
               text='Save / Clear', font=17,
               width=25, background='lightgrey',
               command=self.main_rem).grid(row=3, column=2)

        Button(self.main,
               text='Choose file', font=17,
               width=50, background='lightgrey',
               command=self.myfile).grid(row=3, column=0, columnspan=2)

        self.canv = Canvas(self.main, background='#CFCFCF', width=750, height=450)
        self.canv.grid(row=0, rowspan=3, column=1, columnspan=3)
        self.canv.create_text(370, 220, text='File not found',
                              font=20, fill='grey')

        self.menu = Menu(self.main)
        self.main.configure(menu=self.menu)
        first_item = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Menu',
                              menu=first_item)
        first_item.add_command(label='Open from file',
                               command=self.open_file)

    # ----------------------------------------------------------------------------------

    def myfile(self):
        '''Вводимо назву нового файлу для збереження даних про малюнок'''
        self.top = Toplevel(self.main)
        self.top.geometry('100x80+635+490')
        Label(self.top,
              text='File name:', font=17).pack()
        self.entr = Entry(self.top)
        self.entr.pack()
        Button(self.top,
               text='Create', font=17,
               command=self.newfile).pack()

    def newfile(self):
        '''Створюємо новий файл для збереження даних про малюнок'''
        self.data_name = self.entr.get()
        self.data_name += '.txt'
        with open(self.data_name, 'w') as F:
            pass
        self.top.destroy()
        self.canv.delete('all')
        self.canv.configure(background='white')

    def main_rem(self):
        '''Полотно повертається до початкового вигляду'''
        self.canv.delete('all')
        self.canv.create_text(370, 220, text='File not found',
                              font=20, fill='grey')
        self.canv.configure(background='#CFCFCF')

    def open_file(self):
        '''Зображує малюнок відтворюючи дані з файлу fname, доповнює їх новими'''
        fname = askopenfilename()
        with open(fname, 'r') as F:
            self.canv.delete('all')
            self.canv.configure(background='white')
            Q = F.readlines()
            for line in Q:
                q = line.split()
                if q[0] == 'line':
                    self.canv.create_line(q[1], q[2], q[3], q[4], fill=q[6], width=q[5])
                elif q[0] == 'rectangle':
                    self.canv.create_rectangle(q[1], q[2], q[3], q[4], outline=q[6], width=q[5])
                elif q[0] == 'oval':
                    self.canv.create_oval(q[1], q[2], q[3], q[4], outline=q[6], width=q[5])
        self.data_name = fname

    def exit(self):
        '''Знищує головне вікно'''
        self.main.destroy()

    # ---------------------------------------------------------------------------------------------

    def draw_line(self):
        '''Створюємо вікно для вводу даних про лінію'''
        self.LINE_wind = Toplevel(self.main)
        self.LINE_wind.grab_set()
        self.main_LINE()

    def main_LINE(self):

        self.line_coords = []
        self.LINE_wind.title('Line')
        self.LINE_wind.geometry('125x130+635+152')
        self.LINE_wind.resizable(0, 0)

        Label(self.LINE_wind,
              text='Line width:', font=17).grid(row=0)
        self.ent_line = Entry(self.LINE_wind)
        self.ent_line.grid(row=1)

        Button(self.LINE_wind,
               text='Line color', font=17,
               command=self.line_color).grid(row=2)

        self.canv_line = Canvas(self.LINE_wind, width=100, height=5)
        self.canv_line.grid(row=3)

        Button(self.LINE_wind,
               text='Save', font=17,
               command=self.line_rem).grid(row=4)

        self.canv.bind('<1>', self.line_click)

    def line_checker(self):
        x1 = self.line_coords[0][0]
        y1 = self.line_coords[0][1]
        x2 = self.line_coords[1][0]
        y2 = self.line_coords[1][1]
        self.canv.create_line(x1, y1, x2, y2, fill=self.line_col, width=self.line_width)
        with open(self.data_name, 'a') as F:
            print('line', x1, y1, x2, y2, self.line_width, self.line_col, file=F)

    def line_click(self, event):
        xx = int(event.x)
        yy = int(event.y)
        if len(self.line_coords) < 2:
            self.canv.create_oval(xx - 3, yy - 3, xx + 3, yy + 3, fill='red')
            self.line_coords.append([xx, yy])
        elif len(self.line_coords) == 2:
            self.line_checker()

    def line_rem(self):
        if self.ent_line.get() == '':
            showwarning('Warning', 'Chose line width firstly!')
        elif self.line_col == 'grey':
            showwarning('Warning', 'Chose line color firstly!')
        elif self.canv['bg'] != 'white':
            showwarning('Warning', 'Chose file firstly!')
        else:
            self.line_width = int(self.ent_line.get())
            self.LINE_wind.destroy()

    def line_color(self):
        t, self.line_col = askcolor()
        self.canv_line.configure(background=self.line_col)

    # ----------------------------------------------------------------------------

    def draw_rect(self):
        self.RECT_wind = Toplevel(self.main)
        self.RECT_wind.grab_set()
        self.main_RECT()

    def rect_checker(self):
        x1 = self.rect_coords[0][0]
        y1 = self.rect_coords[0][1]
        x2 = self.rect_coords[1][0]
        y2 = self.rect_coords[1][1]
        self.canv.create_rectangle(x1, y1, x2, y2, outline=self.rect_col, width=self.rect_width)
        with open(self.data_name, 'a') as F:
            print('rectangle', x1, y1, x2, y2, self.rect_width, self.rect_col, file=F)

    def rect_click(self, event):
        xx = int(event.x)
        yy = int(event.y)
        if len(self.rect_coords) < 2:
            self.canv.create_oval(xx - 3, yy - 3, xx + 3, yy + 3, fill='red')
            self.rect_coords.append([xx, yy])
        elif len(self.rect_coords) == 2:
            self.rect_checker()

    def main_RECT(self):
        self.rect_coords = []
        self.RECT_wind.title('Rectangle')
        self.RECT_wind.geometry('125x130+635+300')
        self.RECT_wind.resizable(0, 0)

        Label(self.RECT_wind,
              text='Line width:', font=17).grid(row=0)
        self.ent_rect = Entry(self.RECT_wind)
        self.ent_rect.grid(row=1)

        Button(self.RECT_wind,
               text='Line color', font=17,
               command=self.rect_color).grid(row=2)

        self.canv_rect = Canvas(self.RECT_wind, width=100, height=5)
        self.canv_rect.grid(row=3)

        Button(self.RECT_wind,
               text='Save', font=17,
               command=self.rect_rem).grid(row=4)

        self.canv.bind('<1>', self.rect_click)

    def rect_rem(self):
        if self.ent_rect.get() == '':
            showwarning('Warning', 'Chose line width firstly!')
        elif self.rect_col == 'grey':
            showwarning('Warning', 'Chose line color firstly!')
        elif self.canv['bg'] != 'white':
            showwarning('Warning', 'Chose file firstly!')
        else:
            self.rect_width = int(self.ent_rect.get())
            self.RECT_wind.destroy()

    def rect_color(self):
        t, self.rect_col = askcolor()
        self.canv_rect.configure(background=self.rect_col)

    # -----------------------------------------------------------------------------
    def draw_oval(self):
        self.OVAL_wind = Toplevel(self.main)
        self.OVAL_wind.grab_set()
        self.main_OVAL()

    def main_OVAL(self):

        self.oval_coords = []
        self.OVAL_wind.title('Oval')
        self.OVAL_wind.geometry('125x130+635+440')
        self.OVAL_wind.resizable(0, 0)

        Label(self.OVAL_wind,
              text='Line width:', font=17).grid(row=0)
        self.ent_oval = Entry(self.OVAL_wind)
        self.ent_oval.grid(row=1)

        Button(self.OVAL_wind,
               text='Line color', font=17,
               command=self.oval_color).grid(row=2)

        self.canv_oval = Canvas(self.OVAL_wind, width=100, height=5)
        self.canv_oval.grid(row=3)

        Button(self.OVAL_wind,
               text='Save', font=17,
               command=self.oval_rem).grid(row=4)

        self.canv.bind('<1>', self.oval_click)

    def oval_checker(self):
        x1 = self.oval_coords[0][0]
        y1 = self.oval_coords[0][1]
        x2 = self.oval_coords[1][0]
        y2 = self.oval_coords[1][1]
        self.canv.create_oval(x1, y1, x2, y2, outline=self.oval_col, width=self.oval_width)
        with open(self.data_name, 'a') as F:
            print('oval', x1, y1, x2, y2, self.oval_width, self.oval_col, file=F)

    def oval_click(self, event):
        xx = int(event.x)
        yy = int(event.y)
        if len(self.oval_coords) < 2:
            self.canv.create_oval(xx - 3, yy - 3, xx + 3, yy + 3, fill='red')
            self.oval_coords.append([xx, yy])
        elif len(self.oval_coords) == 2:
            self.oval_checker()

    def oval_rem(self):
        if self.ent_oval.get() == '':
            showwarning('Warning', 'Chose line width firstly!')
        elif self.oval_col == 'grey':
            showwarning('Warning', 'Chose line color firstly!')
        elif self.canv['bg'] != 'white':
            showwarning('Warning', 'Chose file firstly!')
        else:
            self.oval_width = int(self.ent_oval.get())
            self.OVAL_wind.destroy()

    def oval_color(self):
        t, self.oval_col = askcolor()
        self.canv_oval.configure(background=self.oval_col)


# ---------------------------------------------------------------------------
if __name__ == '__main__':
    top = Tk()
    A = Redactor(top)
    top.mainloop()


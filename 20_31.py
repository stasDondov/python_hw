from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
import codecs

class CodeViewer:

    def __init__(self, main):
        self.main = main
        self.init_main()

    def init_main(self):
        self.main.title('CodeViewer')
        self.main.geometry('790x425+300+200')
        self.main.resizable(0, 0)

        Button(self.main,
               width=17, background='grey',
               text='Колір ключових слів', font=15,
               command=self.color1).grid(row=0, column=3)
        self.kw_color = '#ffffff'
        self.kw_canv = Canvas(self.main,
                              width=20, height=20, background=self.kw_color)
        self.kw_canv.grid(row=1, column=3)

        Button(self.main,
               width=17, background='grey',
               text='Колір рядків', font=15,
               command=self.color2).grid(row=2, column=3)
        self.str_color = '#ffffff'
        self.str_canv = Canvas(self.main,
                               width=20, height=20, background=self.str_color)
        self.str_canv.grid(row=3, column=3)

        Button(self.main,
               width=17, background='grey',
               text='Колір коментарів', font=15,
               command=self.color3).grid(row=4, column=3)
        self.com_color = '#ffffff'
        self.com_canv = Canvas(self.main,
                               width=20, height=20, background=self.com_color)
        self.com_canv.grid(row=5, column=3)

        Button(self.main,
               width=17, background='grey',
               text='Колір іншого', font=15,
               command=self.color4).grid(row=6, column=3)
        self.oth_color = '#ffffff'
        self.oth_canv = Canvas(self.main,
                               width=20, height=20, background=self.oth_color)
        self.oth_canv.grid(row=7, column=3)

        self.text = Text(self.main, width=75)
        self.text.grid(row=0, rowspan=8, column=0, columnspan=2)

        self.scrl = Scrollbar(self.main, orient=VERTICAL)
        self.scrl.grid(row=0, rowspan=8, column=2)
        self.scrl.config(command=self.text.yview)

        Button(self.main,
               text='Вибрати файл', font=15,
               background='lightgrey',
               command=self.file).grid(row=8, column=0, sticky=W)

        Button(self.main,
               text='Exit', font=15,
               background='lightgrey',
               command=self.exit).grid(row=8, column=3, sticky=E)

        Button(self.main,
               text='Очистити', font=15,
               background='lightgrey',
               command=self.clear).grid(row=8, column=1, sticky=E)

    def clear(self):
        self.text.delete('1.0', END)

    def exit(self):
        self.main.destroy()

    def file(self):
        fname = askopenfilename()
        with codecs.open(fname, 'r', encoding='utf-8') as F:
            self.Text = F.readlines()
            for line in range(len(self.Text)):

                self.text.insert(END, self.Text[line])

        kw_list = ['def', 'for', 'if', 'open', 'elif', 'pass', 'in', 'try',
                   'except', 'format', 'self', 'from', 'class', '__init__',
                   'import']

        for line in range(len(self.Text)):
            for key in kw_list:
                s1 = self.Text[line].find(key)
                if s1 != -1:
                    s2 = s1 + len(key)
                    self.text.tag_add('3', '{}.{}'.format(line + 1, s1),
                                      '{}.{}'.format(line + 1, s2))
                    self.text.tag_config('3', background=self.kw_color)

            count_ap = 0  # лічильник лапок
            for sym in range(len(self.Text[line])):
                if self.Text[line][sym] == "'" or self.Text[line][sym] == '"':

                    if count_ap % 2 == 0:
                        s = self.Text[line][sym + 1:]
                        try:
                            ind = s.index(self.Text[line][sym]) + 2
                            self.text.tag_add('2', '{}.{}'.format(line + 1, sym),
                                              '{}.{}'.format(line + 1, sym + ind))
                            self.text.tag_config('2', background=self.str_color)
                        except ValueError:
                            pass

                    count_ap += 1

                elif self.Text[line][sym] == '#':
                    self.text.tag_add('1', '{}.{}'.format(line + 1, sym),
                                      '{}.{}'.format(line + 1, len(self.Text[line])))
                    self.text.tag_config('1', background=self.com_color)

    def color1(self):
        t, self.kw_color = askcolor()
        self.kw_canv.configure(background=self.kw_color)

    def color2(self):
        t, self.str_color = askcolor()
        self.str_canv.configure(background=self.str_color)

    def color3(self):
        t, self.com_color = askcolor()
        self.com_canv.configure(background=self.com_color)

    def color4(self):
        t, self.oth_color = askcolor()
        self.oth_canv.configure(background=self.oth_color)


if __name__ == '__main__':
    top = Tk()
    A = CodeViewer(top)
    top.mainloop()


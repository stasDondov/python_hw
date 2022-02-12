from collections import defaultdict
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
from tkinter import _tkinter


class Bank:
    """Обмінник валют"""

    def __init__(self, main):
        
        self.main = main
        self.filename = []
        self.Unique = None
        self.DATA = None
        self.init_main()

    def reader(self):
        """Читає з файлу дані про валюти"""
        
        self.DATA = defaultdict(list)
        with open (self.filename, 'r') as f:
            valutes = f.readlines()
            Big_List = []
            Big_List = [(i.split()) for i in valutes if i not in Big_List]
            Big_List.append(Big_List[0])

            self.Unique = []
            self.Unique = [i.split()[0] for i in valutes if i not in self.Unique]        

        LIST = []
        for i in Big_List:
            LIST.append(i[0])
            LIST.append(i[1])

        for valut in self.Unique:
            var1 = [i[1] for i in Big_List if i[0] == valut][0]
            koef = float([i[2] for i in Big_List if i[0] == valut][0])
            self.DATA[valut].append((var1, koef))
            var2 = ''
            while var2 != valut:
                var2 = [i[1] for i in Big_List if i[0] == var1][0]
                koef *= float([i[2] for i in Big_List if i[0] == var1][0])
                self.DATA[valut].append((var2, koef))
                var1 = var2
            self.DATA[valut] = self.DATA[valut][:len(self.DATA[valut])-1]

    def Chose(self):
        """Вибирає файл для читання"""
        try:
            self.reader()
            self.Child()
        except TypeError:
            showwarning('Warning', 'Виберіть файл!')

    def calc(self):
        """Виводить результат обміну валют"""
        try:
            for i in self.DATA[self.item_1]:
                if i[0] == self.item_2:
                    koef = i[1]
                    ans = float(koef) * float(self.entr_3.get())
                    self.label_4.configure(text='Результат: {0:.2f}'.format(ans))
        except ValueError:
            showerror('Error', 'Введіть число!')
        except AttributeError:
            showerror('Error', 'Введіть число!')
      
    def Exit(self):
        """нищую основне вікно"""
        self.main.destroy()

    def FileName(self):
        """Запам'ятовує імя файлу"""
        self.filename = askopenfilename()

    def init_main(self):
        """Тіло головного вікна"""

        self.main.geometry('+600+300')
        self.main.title('Обмінник валют')
        self.toolbar = Frame()
        self.toolbar.pack(side=TOP, fill=X)
        
        self.label_1 = Label(self.toolbar, text='Валюта 1: ___',font=15)
        self.label_1.grid(row=0, column=0)
        self.label_2 = Label(self.toolbar, text='Валюта 2: ___',font=15)
        self.label_2.grid(row=1, column=0)
        self.label_4 = Label(self.toolbar, text='Результат: ___',font=15)
        self.label_4.grid(row=3, column=0)
        label_3 = Label(self.toolbar, text='Сума:', font=15)
        label_3.grid(row=2, column=0)

        self.entr_3 = Entry(self.toolbar)
        self.entr_3.grid(row=2, column=1)


        btn_1 = Button(self.toolbar, text='Обчислити', font=15,
                       command=self.calc)
        btn_1.grid(row=4, column=0)

        

        btn_2 = Button(self.toolbar, text='Вибрати валюти',
                       command=self.Chose, font=15)
        btn_2.grid(row=4, column=1)

        
        main_menu = Menu(self.main)
        
        first_item = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label='Menu',
                              menu=first_item)
        first_item.add_command(label='File',
                               command=self.FileName)
        first_item.add_command(label='Exit',
                               command=self.Exit)
        self.main.configure(menu=main_menu)
        

    def Child(self):
        """Створює допоміжне вікно"""
        
        self.child = Toplevel(self.main)
        self.init_child()

    def Quit(self):
        """Вихід з допоміжного вікна"""
        try:
            self.label_1.configure(text='Валюта 1: {}'.format(self.item_1))
            self.label_2.configure(text='Валюта 2: {}'.format(self.item_2))
            self.child.destroy()
        except AttributeError:
            showerror('Error', 'Виберіть 2 валюти!')


    def Go_1(self):
        """Знаходить першу валюту"""
        self.item_1 = self.lst_1.get(ANCHOR)
        self.chk_1['onvalue']=0

    def Go_2(self):
        """Знаходить другу валюту"""
        self.item_2 = self.lst_2.get(ANCHOR)
        self.chk_2['onvalue']=0
    
    def init_child(self):
        """Тіло допоміжного вікна"""

        self.child.geometry('+580+165')
        self.child.title('Вибрати валюти')

        self.chk_1 = Checkbutton(self.child,
                            text='Валюта 1',
                            onvalue=1)
        self.chk_1.grid(row=0, column=0)

        self.chk_2 = Checkbutton(self.child,
                            text='Валюта 2',
                            onvalue=1)
        self.chk_2.grid(row=0, column=2)

        svert_1 = Scrollbar(self.child)
        svert_1.grid(row=1, column=1)
        self.lst_1 = Listbox(self.child, height=3, selectmode=SINGLE)
        
        for i in self.Unique:
            self.lst_1.insert(END, i)

        self.lst_1.grid(row=1, column=0)
        svert_1.config(command=self.lst_1.yview)

        svert_2 = Scrollbar(self.child)
        svert_2.grid(row=1, column=3)
        self.lst_2 = Listbox(self.child,height=3,selectmode=SINGLE)
        
        for i in self.Unique:
            self.lst_2.insert(END, i)

        self.lst_2.grid(row=1, column=2)
        svert_2.config(command=self.lst_2.yview)
   
        
        self.lst_1.bind('<<ListboxSelect>>', lambda x: self.Go_1())
        self.lst_2.bind('<<ListboxSelect>>', lambda x: self.Go_2())        
            
        btn_1 = Button(self.child,
                       text='Запам\'ятати',
                       command=self.Quit,
                       width=15, height=1, font=15)
        btn_1.grid(row=3, columnspan=4)
        


if __name__ == '__main__':
    top = Tk()
    B = Bank(top)
    top.mainloop()

#-------------------------------------------------------------
# Для тестування рекомендовано виконувати дії в наступному порядку:
# 1) Menu -> File, обираєте файл для читання
# 2) Вибрати валюти -> вибираєте валюту 1, валюту 2 -> Запам'ятати
# 3) Вводите суму -> Обчислити
# 4) Menu -> Exit


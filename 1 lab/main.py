from tkinter import *
from tkinter import messagebox
import logic
import re
_a: list()
_b: list()
func1 = list()
func2 = list()
dop1 = list()
dop2 = list()
lenght1 = []
lenght2 = []
leng: float
alpha1 = list()
alpha2 = list()


def parse(a):
    content = re.findall('([-+]?\d*\.\d+|\d+)', a)
    spisok = []
    exec("spisok.extend(content)")
    for i in range (0, len(spisok)):
        spisok[i] = float(spisok[i])
        i += 1
    return spisok
def clicked_spisokA():
    a = text1.get()
    b = parse(a)
    dlina = len(b)
    lenght = []
    for i in range(0, dlina):
        lenght.append(i+1)

    sp = logic.SpisokA(b, min(b), max(b))

    func = sp.func_prinA()
    global lenght1
    lenght1 = lenght
    global func1
    func1 = func
    global leng
    global _a
    _a = b
    leng = len(lenght1)

    logic.create_func_graph(func1, lenght1, "A")

def clicked_dopA():
    dop = logic.dop(func1)

    global dop1
    dop1 = dop

    logic.create_dop_graph(dop, lenght1, "A")

def clicked_concentrateA():

    con = logic.concentrate(func1)

    logic.create_con_graph(con, lenght1, "A")

def clicked_strechingA():
    
    str = logic.stretching(func1)

    logic.create_str_graph(str, lenght1, "A")
def clicked_spisokB():
    a = text2.get()
    b = parse(a)
    dlina = len(b)
    lenght = []
    for i in range(0, dlina):
        lenght.append(i+1)
    
    sp = logic.SpisokB(b, min(b), max(b))

    func = sp.func_prinB()

    global lenght2
    lenght2 = lenght
    global func2
    func2 = func
    global _b
    _b = b

    logic.create_func_graph(func2, lenght2, "B")
def clicked_dopB():
    dop = logic.dop(func2)

    global dop2
    dop2 = dop

    logic.create_dop_graph(dop, lenght2, "B")

def clicked_concentrateB():

    con = logic.concentrate(func2)

    logic.create_con_graph(con, lenght2, "B")
    print(con)

def clicked_strechingB():
    
    str = logic.stretching(func2)

    logic.create_str_graph(str, lenght2, "B")
    print(str)

def clicked_minimum():
    if lenght1!=lenght2:
        messagebox.showerror('Ошибка!', 'Количества элементов в выборках не совпадают')
    
    minimum = logic.minimum(func1, func2)

    logic.create_min_graph(minimum, lenght1, "A и B")


def clicked_maximum():
    if lenght1!=lenght2:
            messagebox.showerror('Ошибка!', 'Количества элементов в выборках не совпадают')

    maximum = logic.maximum(func1, func2)

    logic.create_max_graph(maximum, lenght1, "A и B")

def clicked_difA_B():
    if lenght1!=lenght2:
            messagebox.showerror('Ошибка!', 'Количества элементов в выборках не совпадают')
    
    dif = logic.minimum(func1, dop2)

    logic.create_dif_graph(dif, lenght1, "A и не B")

def clicked_difB_A():
    if lenght1!=lenght2:
            messagebox.showerror('Ошибка!', 'Количества элементов в выборках не совпадают')
    
    dif = logic.minimum(func2, dop1)

    logic.create_dif_graph(dif, lenght1, "Не A и B")

def clicked_numbers():
    window_numbers = Tk()
    window_numbers.title("Меры нечёткости, расстояния и тд")
    window_numbers.geometry("1024x768")

    rast_h = logic.rastH(func1, func2)
    otn_rast_h = logic.otn_rastH(rast_h, leng)
    rast_e = logic.rastE(func1, func2)
    otn_rast_e = logic.otn_rastE(rast_e, leng)
    linIndexA = logic.linInd(func1, leng)
    linIndexB = logic.linInd(func2, leng)
    kvIndexA = logic.kvInd(func1, leng)
    kvIndexB = logic.kvInd(func2, leng)
    merNechEgP1A = logic.merNechEgP1(func1, dop1, leng)
    merNechEgP1B = logic.merNechEgP1(func2, dop2, leng)
    merNechEgP2A = logic.merNechEgP2(func1, dop1, leng)
    merNechEgP2B = logic.merNechEgP2(func2, dop2, leng)
    merNechKosA = logic.merNechKos(func1, dop1)
    merNechKosB = logic.merNechKos(func2, dop2)
    kardChA = logic.kardCh(func1, leng)
    kardChB = logic.kardCh(func2, leng)
    

    hemming_label = Label(window_numbers, text=f'Расстояние Хемминга: {rast_h}')
    hemming_label.grid(row=0, column=2)
    otn_hemming_label = Label(window_numbers, text=f'Относительное расстояние Хэмминга: {otn_rast_h}')
    otn_hemming_label.grid(row=1, column=2)
    rast_e_label = Label(window_numbers, text=f'Евклидово расстояние: {rast_e}')
    rast_e_label.grid(row=2, column=2)
    otn_rast_e_label = Label(window_numbers, text=f'Относительное Евклидово расстояние: {otn_rast_e}')
    otn_rast_e_label.grid(row=3, column=2)
    labelA = Label(window_numbers, text="Множество A")
    labelA.grid(row=5, column=1)
    labelB = Label(window_numbers, text="Множество B")
    labelB.grid(row=5, column=3)
    linIndexA_label = Label(window_numbers, text=f'Линейный индекс нечёткости: {linIndexA}')
    linIndexA_label.grid(row=7, column=1)
    linIndexB_label = Label(window_numbers, text=f'Линейный индекс нечёткости: {linIndexB}')
    linIndexB_label.grid(row=7, column=3)
    kvIndexA_label = Label(window_numbers, text=f'Квадратичный индекс нечёткости: {kvIndexA}')
    kvIndexA_label.grid(row=8, column=1)
    kvIndexB_label = Label(window_numbers, text=f'Квадратичный индекс нечёткости: {kvIndexB}')
    kvIndexB_label.grid(row=8, column=3)
    merNechEgP1A_label = Label(window_numbers, text=f'Мера нечёткости Егера (P1): {merNechEgP1A}')
    merNechEgP1A_label.grid(row=9, column=1)
    merNechEgP1B_label = Label(window_numbers, text=f'Мера нечёткости Егера (P1): {merNechEgP1B}')
    merNechEgP1B_label.grid(row=9, column=3)
    merNechEgP2A_label = Label(window_numbers, text=f'Мера нечёткости Егера (P2): {merNechEgP2A}')
    merNechEgP2A_label.grid(row=10, column=1)
    merNechEgP2B_label = Label(window_numbers, text=f'Мера нечёткости Егера (P2): {merNechEgP2B}')
    merNechEgP2B_label.grid(row=10, column=3)
    merNechKosA_label = Label(window_numbers, text=f'Мера нечёткости Коско: {merNechKosA}')
    merNechKosA_label.grid(row=11, column=1)
    merNechKosB_label = Label(window_numbers, text=f'Мера нечёткости Коско: {merNechKosB}')
    merNechKosB_label.grid(row=11, column=3)
    kardChA_label = Label(window_numbers, text=f'Кардинальное число: {kardChA}')
    kardChA_label.grid(row=12, column=1)
    kardChB_label = Label(window_numbers, text=f'Кардинальное число: {kardChB}')
    kardChB_label.grid(row=12, column=3)
    alphaSlice_Label = Label(window_numbers, text="α-срезы")
    alphaSlice_Label.grid(row=14, column=2)
    entry_alpha_label1 = Label(window_numbers, text="Введите α: ")
    entry_alpha_label1.grid(row=16, column=0)
    entry_alpha_label2 = Label(window_numbers, text="Введите α: ")
    entry_alpha_label2.grid(row=16, column=3)
    entry_alpha1 = Entry(window_numbers, width=8)
    entry_alpha1.grid(row=16, column=1)
    entry_alpha2 = Entry(window_numbers, width=8)
    entry_alpha2.grid(row=16, column=4)

    def clicked_button_alpha1():
        alpha_array = list()
         
        buff = float(entry_alpha1.get())

        alpha_array = logic.alphaSlice(_a, func1, buff)

        global alpha1
        alpha1 = alpha_array

        for i in alpha_array:
            blocked_entry_alpha1.insert(END, str(i) + ", ")

    def clicked_button_alpha2():         
        alpha_array = list()
         
        buff = float(entry_alpha2.get())

        

        alpha_array = logic.alphaSlice(_b, func2, buff)

        global alpha2
        alpha2 = alpha_array

        for i in alpha_array:
            blocked_entry_alpha2.insert(END, str(i) + ",")

    button_alpha1 = Button(window_numbers, text="Определить", command=clicked_button_alpha1)
    button_alpha1.grid(row=16, column=2)
    button_alpha2 = Button(window_numbers, text="Определить", command=clicked_button_alpha2)
    button_alpha2.grid(row=16, column=5)

    blocked_entry_alpha1 = Entry(window_numbers, width=14)
    blocked_entry_alpha1.grid(row=17, column=1)
    blocked_entry_alpha2 = Entry(window_numbers, width=14)
    blocked_entry_alpha2.grid(row=17, column=4)


    window_numbers.mainloop()
window = Tk()
window.title("Лабораторная работа №1")
window.geometry("1024x768")

entry_label1 = Label(window, text="Введите первую выборку ([1, 2, 3 ...]): ")
entry_label1.grid(row=0, column=0)
text1 = Entry(window, width=30)
text1.grid(row=0, column=1)
button_spisokA = Button(window, text="Нажми!", command=clicked_spisokA)
button_spisokA.grid(row=0, column=2)
button_dopA = Button(window, text="Дополнение", command=clicked_dopA)
button_dopA.grid(row=0, column=3)
button_conA = Button(window, text="Концентрация", command=clicked_concentrateA)
button_conA.grid(row=0, column=4)
button_strA = Button(window, text="Растяжение", command=clicked_strechingA)
button_strA.grid(row=0, column=5)
button_difA_B = Button(window, text="Разность A/B", command=clicked_difA_B)
button_difA_B.grid(row=0, column=6)

entry_label2 = Label(window, text="Введите вторую выборку ([1, 2, 3 ...]): ")
entry_label2.grid(row=1, column=0)
text2 = Entry(window, width=30)
text2.grid(row=1, column=1)
button_spisokB = Button(window, text="Нажми!", command=clicked_spisokB)
button_spisokB.grid(row=1, column=2)
button_dopB = Button(window, text="Дополнение", command=clicked_dopB)
button_dopB.grid(row=1, column=3)
button_conB = Button(window, text="Концентрация", command=clicked_concentrateB)
button_conB.grid(row=1, column=4)
button_strB = Button(window, text="Растяжение", command=clicked_strechingB)
button_strB.grid(row=1, column=5)
button_difB_A = Button(window, text="Разность B/A", command=clicked_difB_A)
button_difB_A.grid(row=1, column=6)

button_min = Button(window, text="Пересечение", command=clicked_minimum)
button_min.grid(row=2, column=3)
button_max = Button(window, text="Объединение", command=clicked_maximum)
button_max.grid(row=2, column=4)
button_numbers = Button(window, text="Меры нечёткости, расстояния и тд", command=clicked_numbers)
button_numbers.grid(row=2, column=5)

window.mainloop()

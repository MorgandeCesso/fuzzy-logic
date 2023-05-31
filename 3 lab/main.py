from tkinter import Tk, Label, StringVar, Button, Entry
window = Tk()
window.title("Лабораторная работа №3")
window.geometry("800x450")
text_var = []
entries = []
rows, cols = (8,8)
def makeMatrix(Lenght):
    A = [0] * Lenght
    for i in range(Lenght): 
        A[i] = [0] * Lenght
    return A
def get_Matrix():
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())

    return matrix
x2 = 0
y2 = 0
for i in range(rows):
    text_var.append([])
    entries.append([])
    for j in range(cols):
        text_var[i].append(StringVar())
        entries[i].append(Entry(window, textvariable=text_var[i][j],width=6))
        entries[i][j].place(x=100 + x2, y=50 + y2)
        x2 += 50
    y2 += 30
    x2 = 0
def get_k_index(A):
    b = list()
    a = 0
    for x in range(len(A)):
        for y in range(len(A)):
            a = float(A[y][x]) + a
        b.append(round(a,5))
        a = 0
    return b
def get_r_index(A, w):
    b = list()
    a = 0
    for x in range(len(A)):
        for y in range(len(A)):
            a = (float(A[x][y]) * w[y]) + a
        b.append(round(a,5))
        a = 0
    return b
def get_w_index(a):
    b = list()
    for x in range(len(a)):
        h = float(1/a[x])
        b.append(round(h,5))
    return b
def get_l_index(r,w):
    a = list()
    for x in range(len(r)):
        b = r[x]/w[x]
        a.append(round(b,5))
    return a
def max_len(l):
    a = 0
    for x in range(len(l)):
        a = a + l[x]
    return round((a /len(l)),5)
def toch(maxl, l):
    a = ((maxl - len(l))/len(l))* 100
    return a
def index_sogl(maxl, l):
    a = ((maxl - len(l))/(len(l)-1))
    return round(a,5)
def normalize_matrix(w):
    a = 0
    c = list()
    for x in range(len(w)):
        if w[x] > a:
            a = w[x]
    print(a)
    for y in range(len(w)):
        b = w[y]/a
        c.append(round(b,5))
    return c
def nan():
    A = makeMatrix(10)
    A = get_Matrix()
    k = get_k_index(A)
    print('k')
    print(k)
    print('-------------------------------------------------')
    w = get_w_index(k)
    print('w')
    print(w)
    print('-------------------------------------------------')
    r = get_r_index(A,w)
    print('r')
    print(r)
    print('-------------------------------------------------')
    l = get_l_index(r,w)
    print('l')
    print(l)
    print('-------------------------------------------------')
    maxl = max_len(l)
    print('maxl')
    print(maxl)
    print('-------------------------------------------------')
    tochnost = toch(maxl, l)
    print('toch')
    print(toch)
    print('-------------------------------------------------')
    IS = index_sogl(maxl, l)
    print('IS')
    print(IS)
    print('-------------------------------------------------')
    SS = 1.49
    OS = (IS/SS)*100
    print('OS')
    print(OS)
    print('-------------------------------------------------')
    normw = normalize_matrix(w)
    print('normw')
    print(normw)
    label1 = Label(window, text=f'Вектор K: {k}')    
    label1.place(x=500, y=10)
    label2 = Label(window, text=f'Вектор W: {w}')    
    label2.place(x=500, y=30)
    label3 = Label(window, text=f'Вектор R: {r}')    
    label3.place(x=500, y=50)
    label4 = Label(window, text=f'Вектор Лямбда: {l}')    
    label4.place(x=500, y=70)
    label5 = Label(window, text=f'Лямбда max: {maxl}')    
    label5.place(x=500, y=90)
    label6 = Label(window, text=f'Точность решения: {round(tochnost,5)}%')    
    label6.place(x=500, y=110)
    label7 = Label(window, text=f'Индекс согласованости: {IS}')    
    label7.place(x=500, y=130)
    label8 = Label(window, text=f'Отношение согласованости: {round(OS,5)}%')    
    label8.place(x=500, y=150)
    label9 = Label(window, text=f'Нормализация W: {normw}')    
    label9.place(x=500, y=170)
button= Button(window,text="Вычисление", width=15, command= nan)
button.grid(row=1, column=10)
window.mainloop()
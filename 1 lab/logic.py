import matplotlib.pyplot as plt
from math import sqrt

class SpisokA():
    def __init__(self, spisokA, minA, maxA):
        self.spisokA = spisokA
        self.minA = minA
        self.maxA = maxA

    def func_prinA(self):
        massiv = list()
        for i in self.spisokA:
            if i <= self.minA:
                massiv.append(0)
            elif i >= self.maxA:
                massiv.append(1)
            else:
                j = ((i - self.minA) / (self.maxA - self.minA))
                massiv.append(round(j, 2))
        return massiv

class SpisokB():
    def __init__(self, spisokB, minB, maxB):
        self.spisokB = spisokB
        self.minB = minB
        self.maxB = maxB
    def func_prinB(self):
        massiv = list()
        for i in self.spisokB:
            if i <= self.minB:
                massiv.append(1)
            elif i >= self.maxB:
                massiv.append(0)
            else:
                j = ((self.maxB - i)/(self.maxB - self.minB))
                massiv.append(round(j, 2))
        return massiv


def dop(func):
    massiv = list()
    for i in func:
        j = 1 - i
        massiv.append(abs(round(j, 2)))
    return massiv

def maximum(formulaA, formulaB):
    massiv = list()
    for i in range (0, len(formulaA)):
        if formulaA[i] >= formulaB[i]:
            massiv.append(formulaA[i])
        else:
            massiv.append(formulaB[i])
    return massiv

def minimum(formulaA, formulaB):
    massiv = list()
    for i in range (0, len(formulaA)):
        if formulaA[i] <= formulaB[i]:
            massiv.append(formulaA[i])
        else:
            massiv.append(formulaB[i])
    return massiv

def concentrate(formula):
    massiv = list()
    for i in formula:
        j = i**2
        massiv.append(j)
    return massiv

def stretching(formula):
    massiv = list()
    for i in formula:
        j = i ** 0.5
        massiv.append(j)
    return massiv

def rastH(a, b):
    x = 0
    for i in range(0, len(a)):
        x += abs(a[i]-b[i])
    return x

def otn_rastH(h, len):
    return round(h/len, 5)

def rastE(a, b):
    x = 0
    for i in range(0, len(a)):
        x += ((a[i]-b[i])**2)
    return x

def otn_rastE(e, len):
    return round(e/(sqrt(len)), 5)

def linInd(func, len):
    x = 0
    for i in func:
        if i >= 0.5:
            x += abs(i - 1)
        else:
            x += i
    return round(x * (2/ len), 5)

def kvInd(func, len):
    x = 0
    for i in func:
        if i >= 0.5:
            x += (i - 1) ** 2
        else:
            x += i**2
    return round((sqrt(x)*(2/sqrt(len))), 5)

def merNechEgP1(func, dop, len):
    x = 0
    for i in range(0, len):
        x += abs(func[i]-dop[i])
    return round(1-(x/len), 5)

def merNechEgP2(func, dop, len):
    x = 0
    for i in range(0, len):
        x += ((func[i] - dop[i]) ** 2)
    return round((1 - (sqrt(x)/sqrt(len))), 5)

def merNechKos(func, dop):
    x = 0
    y = 0
    for i in range(0, len(func)):
        if func[i] >=dop[i]:
            x += func[i]
        else:
            x += dop[i]
    for j in range(0, len(func)):
        if func[j]<=dop[j]:
            y += func[j]
        else:
            y += dop[j]
    return round((y/x), 5)

def kardCh(func, len):
    x = 0
    for i in range(0, len):
        x += func[i]
    
    return x

def alphaSlice(spisok, func, a):
    massiv = list()
    for i in range(0, len(spisok)):
        if func[i] >= a:
            massiv.append(spisok[i])
    return massiv

def create_func_graph(func, lenght, name):
    plt.plot(lenght, func, label = f'Принадлежность {name}')
    plt.text(0, 1.1, "Можно зачёт?", fontsize = 12)
    plt.grid(True)
    plt.legend()
    plt.show()

def create_dop_graph(dop, lenght, name):
    plt.plot(lenght, dop, label = f'Дополнение {name}')
    plt.grid(True)
    plt.legend()
    plt.show()

def create_con_graph(con, lenght, name):
    plt.plot(lenght, con, label = f'Концентрация {name}')
    plt.grid(True)
    plt.legend()
    plt.show()

def create_str_graph(str, lenght, name):
    plt.plot(lenght, str, label = f'Растяжение {name}')
    plt.grid(True)
    plt.legend()
    plt.show()

def create_min_graph(min, lenght, name):
    plt.plot(lenght, min, label = f'Пересечение {name}')
    plt.grid(True)
    plt.legend()
    plt.show()

def create_max_graph(max, lenght, name):
    plt.plot(lenght, max, label = f'Объединение {name}')
    plt.grid(True)
    plt.legend()
    plt.show()

def create_dif_graph(dif, lenght, name):
    plt.plot(lenght, dif, label = f'Разность {name}')
    plt.grid(True)
    plt.legend()
    plt.show()
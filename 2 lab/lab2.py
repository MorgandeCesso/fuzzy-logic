import re

def create_matrix(size):
    matrix = [0] * size
    for i in range (size):
        matrix[i] = [0] * size
    return matrix

def dif_matrix(matrix, list, size):
    for i in range(size):
        for j in range(size):
            matrix[i][j] = round(list[i]-list[j], 1)
    return matrix

def dif_ABS_matrix(matrix, list, size):
    for i in range(size):
        for j in range(size):
            matrix[i][j] = round(abs(list[i]-list[j]), 1)
    return matrix

def find_max(matrix, size, case):
    maximum = 0
    if case == 'A':
        for i in range(size):
            for j in range(size):
                if matrix[i][j] <= 0 and matrix[i][j]>=maximum:
                    maximum = matrix[i][j]
    elif case == 'B':
        for i in range(size):
            for j in range(size):
                if matrix[i][j] >= maximum:
                    maximum = matrix[i][j]
    return maximum

def find_min(matrix, size, case):
    minimum = 0
    if case == 'A':
        for i in range(size):
            for j in range(size):
                if matrix[i][j] <=0 and matrix[i][j]<minimum:
                    minimum = matrix[i][j]
    elif case == 'B':
        for i in range(size):
            for j in range(size):
                if matrix[i][j]<minimum:
                    minimum = matrix[i][j]
    return minimum

def dif_matrix_output(matrix, size):
    for i in range(size):
        for j in range(size):
            print(f'{matrix[i][j]} |', end=' ')
        print()

def affilation_matrix(matrix, size, max, min, mid, case):
    if case == 'A':
        for i in range(size):
            for j in range(size):
                if matrix[i][j] < min:
                    matrix[i][j] = 0
                elif matrix[i][j] <= mid and matrix[i][j] >= min:
                    matrix[i][j] = round(2*(((matrix[i][j] - min)/(max-min))**2), 3)
                elif matrix[i][j] < max and matrix[i][j] >= mid:
                    matrix[i][j] = round(1 - 2 * (((matrix[i][j] - max)/(max-min))**2), 3)
                elif matrix[i][j] >= max:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 0
    elif case == 'B':
        for i in range(size):
            for j in range(size):
                if matrix[i][j] <= min:
                    matrix[i][j] = 1
                elif matrix[i][j] <= mid and matrix[i][j] >= min:
                    matrix[i][j] = round(1 - 2*(((matrix[i][j]-min)/(max-min))**2), 3)
                elif matrix[i][j]<=max and matrix[i][j] >=mid:
                    matrix[i][j] = round(2*(((matrix[i][j]-max)/(max-min))**2), 3)
                else:
                    matrix[i][j] = 0
    return matrix

def refl(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i] == 1:
            return False
    return True

def weak_refl(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][j] <= matrix[i][j]:
                return False
    return True

def strong_refl(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][j] < matrix[i][i]:
                return False
    return True

def irefl(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i] == 0:
            return False
    return True

def weak_irefl(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][i] <= matrix[i][j]:
                return False
    return True

def strong_irefl(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if not matrix[i][i] < matrix[i][j]:
                return False
    return True

def sym(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if not matrix[i][j] == matrix[j][i]:
                return False
    return True

def antisym(matrix):
    if not refl(matrix):
        return False
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if i != j:
                if not matrix[i][j] * matrix[j][i] == 0:
                    return False
    return True

def asym(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if not matrix[i][j] * matrix[j][i] == 0:
                return False
    return True

def weak_lin(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                if not (matrix[i][j] + matrix[j][i] - (matrix[i][j]*matrix[j][i]))  > 0:
                    return False
    return True

def strong_lin(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                if not (matrix[i][j] + matrix[j][i] - (matrix[i][j]*matrix[j][i]))  == 1:
                    return False
    return True

def trans(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if not matrix[i][k] >= matrix[i][j] * matrix[j][k]:
                    return False
    return True

def get_relations(matrix, name):
    a = f'Отношение {name} обладает следующими свойствами:'
    if refl(matrix):
        if weak_refl(matrix):
            a += ' слабая рефлексивность, '
        elif strong_refl(matrix):
            a += ' сильная рефлексивность,'
    elif irefl(matrix):
        if weak_irefl(matrix):
            a += ' слабая антирефлексивность, '
        elif strong_irefl(matrix):
            a += ' сильная антирефлексивность,'
    if sym(matrix):
        a += ' симметричность,'
    elif antisym(matrix):
        a += ' антисимметричность,'
    elif asym(matrix):
        a += ' асимметричность,'
    
    if weak_lin(matrix):
        a += ' слабая линейность,'
    elif strong_lin(matrix):
        a += ' сильная линейность,'
    else:
        a += ' не линейно,'
    
    if trans(matrix):
        a += ' транзитивность,'
    else:
        a += ' не транзитивно,'

    if a[-1] == ',':
        a = a[:-1] + '.'

    return a

def parse(a):
    content = re.findall('([-+]?\d*\.\d+|\d+)', a)
    spisok = []
    exec("spisok.extend(content)")
    for i in range (0, len(spisok)):
        spisok[i] = float(spisok[i])
        i += 1
    return spisok

print('Введите множество A: ')
a = input()
print()
print('Введите множество B: ')
b = input()
listA = parse(a)
listB = parse(b)

sizeA = len(listA)
sizeB = len(listB)

matrixA = create_matrix(sizeA)
matrixB = create_matrix(sizeB)

difA = dif_matrix(matrixA, listA, sizeA)
difB = dif_ABS_matrix(matrixB, listB, sizeB)

maxA = find_max(difA, sizeA, 'A')
minA = find_min(difA, sizeA, 'A')
midA = (maxA + minA) / 2

maxB = find_max(difB, sizeB, 'B')
minB = find_min(difB, sizeB, 'B')
midB = (maxB + minB) / 2

affA = affilation_matrix(difA, sizeA, maxA, minA, midA, 'A')
affB = affilation_matrix(difB, sizeB, maxB, minB, midB, 'B')
print('Матрица разностей А')
dif_matrix_output(matrixA, sizeA)
print()
print('Матрица принадлежности A')
dif_matrix_output(affA, sizeA)
print()
print('Матрица разностей B')
dif_matrix_output(matrixB, sizeB)
print('Матрица принадлежности B')
dif_matrix_output(affB, sizeB)
print()
print()
a = get_relations(affA, 'A')
print(a)
b = get_relations(affB, 'B')
print(b)
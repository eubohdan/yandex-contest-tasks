'''26. Самый дешевый путь

Ограничение времени	1 секунда
Ограничение памяти	256Mb

В каждой клетке прямоугольной таблицы N×M записано некоторое число. Изначально игрок находится в
левой верхней клетке. За один ход ему разрешается перемещаться в соседнюю клетку либо вправо, либо
вниз (влево и вверх перемещаться запрещено). При проходе через клетку с игрока берут столько
килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки его пути).
Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.

Формат ввода
Вводятся два числа N и M — размеры таблицы (1≤N≤20, 1≤M≤20). Затем идет N строк по M чисел в каждой —
размеры штрафов в килограммах за прохождение через соответствующие клетки (числа от 0 до 100).
Формат вывода
Выведите минимальный вес еды в килограммах, отдав которую можно попасть в правый нижний угол.'''

n, m = map(int, input().split()) # n строк, m столбцов
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [[1000] * (m + 1)]
for _ in range(n):
    dp.append([1000])
dp[0][1] = 0
for i in range(n):
    for j in range(m):
        dp[i + 1].append(min(dp[i+1][j], dp[i][j+1]) + lst[i][j])
print(dp[-1][-1])
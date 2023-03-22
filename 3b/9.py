'''9. Сумма в прямоугольнике

Ограничение времени	3 секунды
Ограничение памяти	256Mb

Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы
N×M в прямоугольнике с левым верхним углом (x1, y1) и правым нижним (x2, y2)

Формат ввода
В первой строке находится числа N, M размеры матрицы (1 ≤ N, M ≤ 1000) и K — количество запросов
(1 ≤ K ≤ 100000). Каждая из следующих N строк содержит по M чисел`— элементы соответствующей строки
матрицы (по модулю не превосходят 1000). Последующие K строк содержат по 4 целых числа, разделенных
пробелом x1 y1 x2 y2 — запрос на сумму элементов матрице в прямоугольнике (1 ≤ x1 ≤ x2 ≤ N, 1 ≤ y1 ≤ y2 ≤ M)

Формат вывода
Для каждого запроса на отдельной строке выведите его результат —
сумму всех чисел элементов матрице в прямоугольнике (x1, y1), (x2, y2)'''

n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = [0] * (n + 1)
for i in range(n + 1):
    b[i] = [0] * (m + 1)
for i in range(n):
    for j in range(m):
        b[i + 1][j + 1] = a[i][j] + b[i][j + 1] + b[i + 1][j] - b[i][j]
x = []
for i in range(k):
    i1, j1, i2, j2 = map(int, input().split())
    c = b[i2][j2] - b[i1 - 1][j2] - b[i2][j1 - 1] + b[i1 - 1][j1 - 1]
    x.append(c)
print(*x, sep='\n')

'''38. Блохи


Ограничение времени	1 секунда
Ограничение памяти	64Mb

На клеточном поле, размером NxM (2 ≤ N, M ≤ 250) сидит Q (0 ≤ Q ≤ 10000) блох в различных клетках.
"Прием пищи" блохами возможен только в кормушке - одна из клеток поля, заранее известная. Блохи
перемещаются по полю странным образом, а именно, прыжками, совпадающими с ходом обыкновенного
шахматного коня. Длина пути каждой блохи до кормушки определяется как количество прыжков.
Определить минимальное значение суммы длин путей блох до кормушки или, если собраться блохам у
кормушки невозможно, то сообщить об этом. Сбор невозможен, если хотя бы одна из блох не может
попасть к кормушке.

Формат ввода
В первой строке входного файла находится 5 чисел, разделенных пробелом: N, M, S, T, Q. N, M -
размеры доски (отсчет начинается с 1); S, T - координаты клетки - кормушки (номер строки и столбца
соответственно), Q - количество блох на доске. И далее Q строк по два числа - координаты каждой блохи.

Формат вывода
Содержит одно число - минимальное значение суммы длин путей или -1, если сбор невозможен.'''

with open('input.txt', 'r') as f:
    n, m, s, t, q = map(int, f.readline().split())
    points = [list(map(int, f.readline().split())) for _ in range(q)]

graph = [[-1] * (m + 1) for _ in range(n + 1)]
graph[s][t] = 0
queue = [[s, t]]
while queue:
    i, j = queue[0]
    if i > 1:
        if j > 2 and graph[i - 1][j - 2] == -1:
            graph[i - 1][j - 2] = graph[i][j] + 1
            queue.append([i - 1, j - 2])
        if j + 2 <= m and graph[i - 1][j + 2] == -1:
            graph[i - 1][j + 2] = graph[i][j] + 1
            queue.append([i - 1, j + 2])
    if i + 1 <= n:
        if j > 2 and graph[i + 1][j - 2] == -1:
            graph[i + 1][j - 2] = graph[i][j] + 1
            queue.append([i + 1, j - 2])
        if j + 2 <= m and graph[i + 1][j + 2] == -1:
            graph[i + 1][j + 2] = graph[i][j] + 1
            queue.append([i + 1, j + 2])
    if i > 2:
        if j > 1 and graph[i - 2][j - 1] == -1:
            graph[i - 2][j - 1] = graph[i][j] + 1
            queue.append([i - 2, j - 1])
        if j + 1 <= m and graph[i - 2][j + 1] == -1:
            graph[i - 2][j + 1] = graph[i][j] + 1
            queue.append([i - 2, j + 1])
    if i + 2 <= n:
        if j > 1 and graph[i + 2][j - 1] == -1:
            graph[i + 2][j - 1] = graph[i][j] + 1
            queue.append([i + 2, j - 1])
        if j + 1 <= m and graph[i + 2][j + 1] == -1:
            graph[i + 2][j + 1] = graph[i][j] + 1
            queue.append([i + 2, j + 1])
    queue.pop(0)
res = 0
for point in points:
    if graph[point[0]][point[1]] == -1:
        res = -1
        break
    else:
        res += graph[point[0]][point[1]]
print(res)
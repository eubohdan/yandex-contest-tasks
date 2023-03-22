'''39. Путь спелеолога

Ограничение времени	1 секунда
Ограничение памяти	64Mb

Пещера представлена кубом, разбитым на N частей по каждому измерению (то есть на N3 кубических клеток).
Каждая клетка может быть или пустой, или полностью заполненной камнем. Исходя из положения спелеолога
в пещере, требуется найти, какое минимальное количество перемещений по клеткам ему требуется, чтобы
выбраться на поверхность. Переходить из клетки в клетку можно, только если они обе свободны и имеют общую грань.

Формат ввода
В первой строке содержится число N (1 ≤ N ≤ 30). Далее следует N блоков. Блок состоит из пустой
строки и N строк по N символов: # - обозначает клетку, заполненную камнями, точка - свободную клетку.
Начальное положение спелеолога обозначено заглавной буквой S. Первый блок представляет верхний уровень
пещеры, достижение любой свободной его клетки означает выход на поверхность. Выход на поверхность всегда возможен.

Формат вывода
Вывести одно число - длину пути до поверхности.

Пример входных данных
3

###
###
.##

.#.
.#S
.#.

###
...
###
'''

graph = []
with open('input.txt', 'r') as f:
    n = int(f.readline())
    graph.append([['#'] * (n + 2) for _ in range(n + 2)])
    for i in range(n):
        f.readline()
        graph.append([['#'] * (n + 2)])
        for j in range(n):
            graph[-1].append(['#'])
            string = f.readline().rstrip()
            for k, x in enumerate(string):
                if x == 'S':
                    start_point = [i + 1, j + 1, k + 1]
                    graph[-1][-1].append(0)
                else:
                    graph[-1][-1].append(x)
            graph[-1][-1].append('#')
        graph[-1].append(['#'] * (n + 2))
    graph.append([['#'] * (n + 2) for _ in range(n + 2)])

queue, flag = [start_point], False
while queue and not flag:
    i, j, k = queue[0]
    for q in [[i, j, k + 1], [i, j, k - 1], [i, j + 1, k], [i, j - 1, k], [i + 1, j, k], [i - 1, j, k]]:
        if graph[q[0]][q[1]][q[2]] == '.':
            if q[0] == 1:
                flag = True
                res = graph[i][j][k] + 1
            graph[q[0]][q[1]][q[2]] = graph[i][j][k] + 1
            queue.append(q)
    queue.pop(0)

print(res)

'''34. Топологическая сортировка


Ограничение времени	2 секунды
Ограничение памяти	256Mb

Дан ориентированный граф. Необходимо построить топологическую сортировку.

Формат ввода
В первой строке входного файла два натуральных числа N и M (1 ≤ N, M ≤ 100000) —
количество вершин и рёбер в графе соответственно. Далее в M строках перечислены рёбра
графа. Каждое ребро задаётся парой чисел — номерами начальной и конечной вершин соответственно.

Формат вывода
Выведите любую топологическую сортировку графа в виде последовательности номеров вершин
(перестановка чисел от 1 до N). Если топологическую сортировку графа построить невозможно, выведите -1.'''

from threading import stack_size
from sys import setrecursionlimit


setrecursionlimit(1000000)
mb = 1024 * 1024
stack_size(128 * mb)


def dfs(graph, visited, now):
    global srtd_grph
    global flag
    visited[now] = 1
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)
            if not flag:
                return False
        elif visited[neig] == 1:
            flag = False
            return False
    visited[now] = 2
    srtd_grph.append(now)


flag = True
with open('input.txt', 'r') as s:
    n, m = map(int, s.readline().split())
    graph_lst = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    srtd_grph = []
    for i in range(m):
        frst, lst = map(int, s.readline().split())
        graph_lst[frst].append(lst)


for i, x in enumerate(visited):
    if not x:
        res = dfs(graph=graph_lst, visited=visited, now=i)
        if res is False:
            break
if flag:
    print(*srtd_grph[::-1])
else:
    print(-1)

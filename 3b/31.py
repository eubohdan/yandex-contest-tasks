'''31. Поиск в глубину

	                Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	256Mb

Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить
компоненту связности, содержащую первую вершину.

Формат ввода
В первой строке записаны два целых числа N (1 ≤ N ≤ 103) и M (0 ≤ M ≤ 5 * 105) —
количество вершин и ребер в графе. В последующих M строках перечислены ребра — пары чисел,
определяющие номера вершин, которые соединяют ребра.

Формат вывода
В первую строку выходного файла выведите число K — количество вершин в компоненте связности.
Во вторую строку выведите K целых чисел — вершины компоненты связности, перечисленные в порядке
возрастания номеров.

Пример входных данных
4 5
2 2
3 4
2 3
1 3
2 4
'''

from threading import stack_size
from sys import setrecursionlimit

mb = 1024 * 1024
stack_size(128 * mb)
setrecursionlimit(10000)


def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)

with open('input.txt', 'r') as s:
    # s = s.read()
    n, m = map(int, s.readline().split())
    graph_lst = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for i in range(m):
        frst, lst = map(int, s.readline().split())
        graph_lst[frst].append(lst)
        graph_lst[lst].append(frst)

for i in graph_lst[1]:
    dfs(graph=graph_lst, visited=visited, now=i)
res = []
for i, x in enumerate(visited):
    if x:
        res.append(i)
if not res:
    res.append(1)
print(len(res))
print(*res)

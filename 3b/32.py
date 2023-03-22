'''32. Компоненты связности

	                Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	    256Mb

Дан неориентированный невзвешенный граф, состоящий из N вершин и M ребер.
Необходимо посчитать количество его компонент связности и вывести их.

Формат ввода
Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000).
В следующих M строках записаны по два числа i и j (1 ≤ i, j ≤ N), которые означают,
что вершины i и j соединены ребром.

Формат вывода
В первой строчке выходного файла выведите количество компонент связности. Далее
выведите сами компоненты связности в следующем формате: в первой строке количество
вершин в компоненте, во второй - сами вершины в произвольном порядке.

Пример входных данных
6 4
4 2
1 4
6 4
3 6
'''

from sys import setrecursionlimit
setrecursionlimit(30000)


def dfs(graph, visited, now, components):
    visited[now] = True
    components[-1].append(now)
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, components)


with open('input.txt', 'r') as s:
    n, m = map(int, s.readline().split())
    graph_lst = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    components = []
    for i in range(m):
        frst, lst = map(int, s.readline().split())
        graph_lst[frst].append(lst)
        graph_lst[lst].append(frst)


for i, x in enumerate(visited):
    if not x:
        components.append(list())
        dfs(graph=graph_lst, visited=visited, now=i, components=components)

print(len(components))
for i in components:
    print(len(i))
    print(*i)

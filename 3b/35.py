'''35. Поиск цикла

	                Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	    256Mb

Дан неориентированный граф. Требуется определить, есть ли в нем цикл, и, если есть, вывести его.

Формат ввода
В первой строке дано одно число n — количество вершин в графе (1≤ n ≤500). Далее в n строках задан
сам граф матрицей смежности.

Формат вывода
Если в иcходном графе нет цикла, то выведите «NO». Иначе, в первой строке выведите «YES», во второй
строке выведите число k — количество вершин в цикле, а в третьей строке выведите k различных чисел —
номера вершин, которые принадлежат циклу в порядке обхода (обход можно начинать с любой вершины цикла).
Если циклов несколько, то выведите любой.'''

def dfs(graph, visited, now, last=None):
    global flag
    global way
    visited[now] = 1
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, last=now)
            if flag:
                if len(way) == 1 or way[0] != way[-1]:
                    way.append(neig)
                return True
        elif visited[neig] == 1 and neig != last:
            way.append(neig)
            flag = True
            return True
    visited[now] = 2


flag = False
with open('input.txt', 'r') as s:
    n = int(s.readline())
    graph_lst = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    way = []
    for i in range(n):
        for j, x in enumerate(list(map(int, s.readline().split()))):
            if x:
                graph_lst[i + 1].append(j + 1)

for i, x in enumerate(visited):
    if not x:
        res = dfs(graph=graph_lst, visited=visited, now=i)
        if res is True:
            break
if flag:
    print('YES')
    if way[0] == way[-1]:
        way = way[:-1]
    print(len(way))
    print(*way)
else:
    print('NO')
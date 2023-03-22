'''37. Путь в графе

                    Все языки	Python 3.6
Ограничение времени	1 секунда	5 секунд
Ограничение памяти	64Mb	    256Mb

В неориентированном графе требуется найти минимальный путь между двумя вершинами.

Формат ввода
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100).
Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра).
Далее задаются номера двух вершин – начальной и конечной.

Формат вывода
Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти),
а потом сам путь. Если путь имеет длину 0, то его выводить не нужно, достаточно вывести длину.
Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.

Пример входных данных
10
0 1 0 0 0 0 0 0 0 0
1 0 0 1 1 0 1 0 0 0
0 0 0 0 1 0 0 0 1 0
0 1 0 0 0 0 1 0 0 0
0 1 1 0 0 0 0 0 0 1
0 0 0 0 0 0 1 0 0 1
0 1 0 1 0 1 0 0 0 0
0 0 0 0 0 0 0 0 1 0
0 0 1 0 0 0 0 1 0 0
0 0 0 0 1 1 0 0 0 0
5 4
'''

graph = [[]]
with open('input.txt', 'r') as s:
    n = int(s.readline())
    for i in range(n):
        graph.append([])
        for j, x in enumerate(map(int, s.readline().split())):
            if x:
                graph[i + 1].append(j + 1)
    first_point, last_point = map(int, s.readline().split())

if first_point != last_point:
    visited = [False for _ in range(n + 1)]
    last = [False for _ in range(n + 1)]
    visited[first_point] = 0
    last[first_point] = -1
    cntr, queue = 0, [first_point]
    while visited[last_point] is False and queue:
        for neig in graph[queue[0]]:
            if visited[neig] is False:
                visited[neig] = visited[queue[0]] + 1
                last[neig] = queue[0]
                queue.append(neig)
        queue.pop(0)
    if visited[last_point]:
        print(visited[last_point])
        way = [last_point]
        x = last_point
        while way[-1] != first_point:
            way.append(last[x])
            x = way[-1]
        print(*way[::-1])
    else:
        print(-1)
else:
    print(0)
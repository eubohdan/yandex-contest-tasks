'''33. Списывание


                    Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	    256Mb

Во время контрольной работы профессор Флойд заметил, что некоторые студенты обмениваются записками.
Сначала он хотел поставить им всем двойки, но в тот день профессор был добрым, а потому решил
разделить студентов на две группы: списывающих и дающих списывать, и поставить двойки только первым.

У профессора записаны все пары студентов, обменявшихся записками. Требуется определить, сможет ли
он разделить студентов на две группы так, чтобы любой обмен записками осуществлялся от студента
одной группы студенту другой группы.

Формат ввода
В первой строке находятся два числа N и M — количество студентов и количество пар студентов,
обменивающихся записками (1 ≤ N ≤ 102, 0 ≤ M ≤ N(N−1)/2).

Далее в M строках расположены описания пар студентов: два числа, соответствующие номерам
студентов, обменивающихся записками (нумерация студентов идёт с 1). Каждая пара студентов
перечислена не более одного раза.

Формат вывода
Необходимо вывести ответ на задачу профессора Флойда. Если возможно разделить студентов на две
группы - выведите YES; иначе выведите NO.'''

from sys import setrecursionlimit
setrecursionlimit(30000)


def dfs(graph, visited, now, last_color):
    global flag
    visited[now] = 3 - last_color
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, 3 - last_color)
        else:
            if visited[now] == visited[neig]:
                flag = False
                return False



flag = True
with open('input.txt', 'r') as s:
    n, m = map(int, s.readline().split())
    graph_lst = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    for i in range(m):
        frst, lst = map(int, s.readline().split())
        graph_lst[frst].append(lst)
        graph_lst[lst].append(frst)


for i, x in enumerate(visited):
    if not x:
        res = dfs(graph=graph_lst, visited=visited, now=i, last_color=2)
        if res is False:
            break
print(('NO', 'YES')[flag])

'''24. Покупка билетов

Ограничение времени	1 секунда
Ограничение памяти	64Mb

За билетами на премьеру нового мюзикла выстроилась очередь из N человек, каждый из которых хочет
купить 1 билет. На всю очередь работала только одна касса, поэтому продажа билетов шла очень
медленно, приводя «постояльцев» очереди в отчаяние. Самые сообразительные быстро заметили, что,
как правило, несколько билетов в одни руки кассир продаёт быстрее, чем когда эти же билеты
продаются по одному. Поэтому они предложили нескольким подряд стоящим людям отдавать деньги
первому из них, чтобы он купил билеты на всех.

Однако для борьбы со спекулянтами кассир продавала не более 3-х билетов в одни руки, поэтому
договориться таким образом между собой могли лишь 2 или 3 подряд стоящих человека.

Известно, что на продажу i-му человеку из очереди одного билета кассир тратит Ai секунд, на
продажу двух билетов — Bi секунд, трех билетов — Ci секунд. Напишите программу, которая подсчитает
минимальное время, за которое могли быть обслужены все покупатели.

Обратите внимание, что билеты на группу объединившихся людей всегда покупает первый из них. Также
никто в целях ускорения не покупает лишних билетов (то есть билетов, которые никому не нужны).

Формат ввода
На вход программы поступает сначала число N — количество покупателей в очереди (1 ≤ N ≤ 5000).
Далее идет N троек натуральных чисел Ai, Bi, Ci. Каждое из этих чисел не превышает 3600.
Люди в очереди нумеруются, начиная от кассы.

Формат вывода
Требуется вывести одно число — минимальное время в секундах, за которое могли быть обслужены
все покупатели.

Пример входных данных
5
5 10 15
2 10 15
5 5 5
20 20 1
20 1 1
'''

n, queue = int(input()), []
for i in range(n):
    queue.append(list(map(int, input().split())))
queue[0].append(queue[0][0])
if len(queue) > 1:
    queue[1].append(min(queue[0][0] + queue[1][0], queue[0][1]))
if len(queue) > 2:
    queue[2].append(min(queue[0][0] + queue[1][0] + queue[2][0], queue[0][1] + queue[2][0], queue[0][0] + queue[1][1], queue[0][2]))
if len(queue) > 3:
    for i in range(3, len(queue)):
        queue[i].append(min(queue[i-1][-1] + queue[i][0], queue[i-2][-1] + queue[i-1][1], queue[i-3][-1] + queue[i-2][2]))
print(queue[-1][-1])

'''25. Гвоздики

Ограничение времени	1 секунда
Ограничение памяти	64Mb

В дощечке в один ряд вбиты гвоздики. Любые два гвоздика можно соединить ниточкой. Требуется
соединить некоторые пары гвоздиков ниточками так, чтобы к каждому гвоздику была привязана
хотя бы одна ниточка, а суммарная длина всех ниточек была минимальна.

Формат ввода
В первой строке входных данных записано число N — количество гвоздиков (2 ≤ N ≤ 100).
В следующей строке заданы N чисел — координаты всех гвоздиков (неотрицательные целые
числа, не превосходящие 10000).

Формат вывода
Выведите единственное число — минимальную суммарную длину всех ниточек.

Пример входных данных
6
3 13 12 4 14 6
'''

n = int(input())
points = sorted(map(int, input().split()))
res = [11111, points[1] - points[0]]
for i in range(2, n):
    res.append(min(res[i-2], res[i-1]) + points[i] - points[i-1])
print(res[-1])

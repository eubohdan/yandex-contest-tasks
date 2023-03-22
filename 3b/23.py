'''23. Калькулятор

Ограничение времени	2 секунды
Ограничение памяти	256Mb

Имеется калькулятор, который выполняет следующие операции:
умножить число X на 2;
умножить число X на 3;
прибавить к числу X единицу.
Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 106.

Формат вывода
В первой строке выходного файла выведите минимальное количество операций. Во второй строке
выведите числа, последовательно получающиеся при выполнении операций. Первое из них должно
быть равно 1, а последнее N. Если решений несколько, выведите любое.

Пример входных данных
5
'''

n, cnt = int(input()), 0
lst, dp, prev = [n], [0], [-1]
while cnt < len(lst):
    if lst[cnt] > 1:
        if not lst[cnt] % 3:
            lst.append(lst[cnt] // 3)
            dp.append(dp[cnt] + 1)
            prev.append(cnt)
        if not lst[cnt] % 2:
            lst.append(lst[cnt] // 2)
            dp.append(dp[cnt] + 1)
            prev.append(cnt)
        if lst[cnt] % 3 == 1 or lst[cnt] % 2 == 1:
            lst.append(lst[cnt] - 1)
            dp.append(dp[cnt] + 1)
            prev.append(cnt)
    else:
        break
    cnt += 1

indexes = {}
for i, x in enumerate(lst):
    if x == 1:
        indexes[dp[i]] = i
x = indexes[min(indexes.keys())]
res = [lst[x]]
while prev[x] != -1:
    x = prev[x]
    res.append(lst[x])
print(min(indexes.keys()))
print(*res)

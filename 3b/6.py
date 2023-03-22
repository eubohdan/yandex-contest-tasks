'''6. Операционные системы lite

Ограничение времени	1 секунда
Ограничение памяти	64Mb

Васин жесткий диск состоит из M секторов. Вася последовательно устанавливал на него различные
операционные системы следующим методом: он создавал новый раздел диска из последовательных секторов,
начиная с сектора номер ai и до сектора bi включительно, и устанавливал на него очередную систему.
При этом, если очередной раздел хотя бы по одному сектору пересекается с каким-то ранее созданным
разделом, то ранее созданный раздел «затирается», и операционная система, которая на него была
установлена, больше не может быть загружена.

Напишите программу, которая по информации о том, какие разделы на диске создавал Вася, определит,
сколько в итоге работоспособных операционных систем установлено и работает в настоящий момент на
Васином компьютере.

Формат ввода
Сначала вводятся натуральное число M — количество секторов на жестком диске (1 ≤ M ≤ 10**9) и целое
число N — количество разделов, которое последовательно создавал Вася (0 ≤ N ≤ 1000). Далее идут
N пар чисел ai и bi, задающих номера начального и конечного секторов раздела (1 ≤ ai ≤ bi ≤ M).

Формат вывода
Выведите одно число — количество работающих операционных систем на Васином компьютере.'''


m, n = int(input()), int(input())
systems, res = [], 1
for i in range(n):
    x = list(map(int, input().split()))
    systems.append(x)
if n:
    common = [systems[-1]]
    for new in systems[::-1]:
        flag = True
        for i in range(len(common)):
            if flag:
                if common[i][0] <= new[0] <= common[i][1] or common[i][0] <= new[1] <= common[i][1] or new[0] <= common[i][0] <= new[1] or new[0] <= common[i][1] <= new[1]:
                    x = common[i] + new
                    common[i] = [min(x), max(x)]
                    flag = False
        if flag:
            res += 1
            common.append(new)
    res = len(common)
else:
    res = 0
print(res)
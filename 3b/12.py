'''12. Правильная скобочная последовательность

Ограничение времени	1 секунда
Ограничение памяти	64Mb

Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа должна
определить, является ли данная скобочная последовательность правильной. Пустая последовательность
явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные.
Если A и B – правильные последовательности, то последовательность AB – правильная.

Формат ввода
В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Формат вывода
Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.

Пример входных данных
([)]
'''

n, count, stack, res = input(), 0, [], True
d = {')': '(', ']': '[', '}': '{'}
for i in n:
    if i in '([{':
        stack.append(i)
        count += 1
    else:
        if stack:
            if stack[-1] != d[i]:
                res = False
                break
            else:
                del stack[-1]
                count -= 1
        else:
            res = False
            break
print(('no', 'yes')[res and count == 0])

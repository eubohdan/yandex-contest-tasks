'''5. Хорошая строка

Ограничение времени	1 секунда
Ограничение памяти	64Mb

На день рождения маленький Ипполит получил долгожданный подарок — набор дощечек с написанными
на них буквами латинского алфавита. Теперь-то ему будет чем заняться долгими вечерами, тем более
что мама обещала подарить ему в следующем году последовательность целых неотрицательных чисел,
если он хорошо освоит этот набор. Ради такого богатства Ипполит готов на многое.

Прямо сейчас юный исследователь полностью поглощён изучением хорошести строк. Хорошестью строки
называется количество позиций от 1 до L - 1 (где L — длина строки), таких, что следующая буква
в строке является следующей по алфавиту. Например, хорошесть строки "abcdefghijklmnopqrstuvwxyz"
равна 25, а строки "abdc" — только 1.

Ипполит размышляет над решением закономерно возникающей задачи: чему равна максимально возможная
хорошесть строки, которую можно собрать, используя дощечки из данного набора? Вы-то и поможете ему
с ней справиться.

Формат ввода
Первая строка ввода содержит единственное целое число N — количество различных букв в наборе
(1≤N≤26). Обратите внимание: в наборе всегда используются N первых букв латинского алфавита.

Следующие N строк содержат целые положительные числа ci — количество букв соответствующего типа
(1≤ci≤10**9). Таким образом, первое число означает количество букв "a", второе число задаёт
количество букв "b" и так далее.

Формат вывода
Выведите единственное целое число — максимально возможную хорошесть строки, которую можно собрать
из имеющихся дощечек.'''


n, x, res = int(input()), [], 0
for _ in range(n):
    x.append(int(input()))
m = min(x)
res += (n - 1) * m
x = [i - m for i in x]
x.append(0)
for i in range(n):
    while x[i] and x[i + 1]:
        last = x.index(0, i)
        mres = min(x[i:last])
        for j in range(i, last):
            x[j] -= mres
        res += mres * (len(range(i, last)) - 1)
print(res)
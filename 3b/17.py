'''17. Игра в пьяницу

Ограничение времени	1 секунда
Ограничение памяти	64Mb

В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной
верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, которые кладутся под
низ его колоды. Тот, кто остается без карт – проигрывает. Для простоты будем считать, что все
карты различны по номиналу, а также, что самая младшая карта побеждает самую старшую карту
("шестерка берет туза"). Игрок, который забирает себе карты, сначала кладет под низ своей колоды
карту первого игрока, затем карту второго игрока (то есть карта второго игрока оказывается внизу
колоды). Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. В
игре участвует 10 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со
значением 0 побеждает карту 9.

Формат ввода
Программа получает на вход две строки: первая строка содержит 5 чисел, разделенных пробелами —
номера карт первого игрока, вторая – аналогично 5 карт второго игрока. Карты перечислены сверху
вниз, то есть каждая строка начинается с той карты, которая будет открыта первой.

Формат вывода
Программа должна определить, кто выигрывает при данной раздаче, и вывести слово first или second,
после чего вывести количество ходов, сделанных до выигрыша. Если на протяжении 106 ходов игра не
заканчивается, программа должна вывести слово botva.'''

first, second, i = list(map(int, input().split())), list(map(int, input().split())), 0
while i not in [len(first), len(second), 999999]:
    if first[i] > second[i]:
        if first[i] == 9 and second[i] == 0:
            second.extend([first[i], second[i]])
        else:
            first.extend([first[i], second[i]])
    else:
        if first[i] == 0 and second[i] == 9:
            first.extend([first[i], second[i]])
        else:
            second.extend([first[i], second[i]])
    i += 1
if i == 999999:
    print('botva')
else:
    print(('first', 'second')[len(second) > len(first)], i)

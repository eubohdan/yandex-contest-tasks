'''4. Контрольная работа

Ограничение времени	1 секунда
Ограничение памяти	64Mb

Петя и Вася — одноклассники и лучшие друзья, поэтому они во всём помогают друг другу.
Завтра у них контрольная по математике, и учитель подготовил целых K вариантов заданий.
В классе стоит один ряд парт, за каждой из них (кроме, возможно, последней) на контрольной
будут сидеть ровно два ученика. Ученики знают, что варианты будут раздаваться строго по
порядку: правый относительно учителя ученик первой парты получит вариант 1, левый — вариант 2,
правый ученик второй парты получит вариант 3 (если число вариантов больше двух) и т.д.
Так как K может быть меньше чем число учеников N, то после варианта K снова выдаётся вариант 1.
На последней парте в случае нечётного числа учеников используется только место 1.

Петя самым первым вошёл в класс и сел на своё любимое место. Вася вошёл следом и хочет получить
такой же вариант, что и Петя, при этом сидя к нему как можно ближе. То есть между ними должно
оказаться как можно меньше парт, а при наличии двух таких мест с равным расстоянием от Пети Вася
сядет позади Пети, а не перед ним. Напишите программу, которая подскажет Васе, какой ряд и какое
место (справа или слева от учителя) ему следует выбрать. Если же один и тот же вариант Вася с
Петей писать не смогут, то выдайте одно число -1.

Формат ввода
В первой строке входных данных находится количество учеников в классе 2≤N≤10**9.
Во второй строке — количество подготовленных для контрольной вариантов заданий 2≤K≤N.
В третьей строке — номер ряда, на который уже сел Петя,
в четвёртой — цифра 1, если он сел на правое место, и 2, если на левое.

Формат вывода
Если Вася никак не сможет писать тот же вариант, что и Петя, то выведите -1.
Если решение существует, то выведите два числа — номер ряда, на который следует сесть Васе,
и 1, если ему надо сесть на правое место, или 2, если на левое. Разрешается использовать
только первые N мест в порядке раздачи вариантов.

Пример входных данных
25
2
1
2'''

pupils, variants, petr_row, petr_side = int(input()), int(input()), int(input()), int(input())
petr_seat = (petr_row - 1) * 2 + petr_side
petr_variant = petr_seat % variants
if not petr_variant:
    petr_variant = variants
vasya_seat_back = petr_seat + variants
vasya_seat_front = petr_seat - variants
vasya_desk_back = [vasya_seat_back // 2 + vasya_seat_back % 2, (2, 1)[vasya_seat_back % 2]]
vasya_desk_front = [vasya_seat_front // 2 + vasya_seat_front % 2, (2, 1)[vasya_seat_front % 2]]
choice = bool(vasya_seat_back > pupils) + bool(vasya_seat_front < 1)
answer = [(vasya_desk_front, vasya_desk_back)[abs(petr_row - vasya_desk_back[0]) <= abs(petr_row - vasya_desk_front[0])], vasya_desk_back if vasya_seat_back <= pupils else vasya_desk_front, [-1]]
print(*answer[choice])

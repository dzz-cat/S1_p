# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = int(input('Введите общее количество журавликов (S):'))
x = int(S / 6)  # По сколько сделали Петя и Сережа
k = int(S - 2 * x)  # Сколько сделала Катя
print(f'Сережа и Петя сделали по {x} журавлика/ов, а Катя - {k} ')
import sys

n = int(input())
signal = list(map(str, sys.stdin.readline().rstrip()))
line_length = n // 5

signal_line = []

zero = [['#', '#', '#'],
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#']]
one = [['#'],
       ['#'],
       ['#'],
       ['#'],
       ['#']]
two = [['#', '#', '#'],
       ['.', '.', '#'],
       ['#', '#', '#'],
       ['#', '.', '.'],
       ['#', '#', '#']]
three = [['#', '#', '#'],
         ['.', '.', '#'],
         ['#', '#', '#'],
         ['.', '.', '#'],
         ['#', '#', '#']]
four = [['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['.', '.', '#']]
five = [['#', '#', '#'],
        ['#', '.', '.'],
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['#', '#', '#']]
six = [['#', '#', '#'],
       ['#', '.', '.'],
       ['#', '#', '#'],
       ['#', '.', '#'],
       ['#', '#', '#']]
seven = [['#', '#', '#'],
         ['.', '.', '#'],
         ['.', '.', '#'],
         ['.', '.', '#'],
         ['.', '.', '#']]
eight = [['#', '#', '#'],
         ['#', '.', '#'],
         ['#', '#', '#'],
         ['#', '.', '#'],
         ['#', '#', '#']]
nine = [['#', '#', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['#', '#', '#']]
for i in range(5):
    signal_line.append(signal[i * line_length:(i + 1) * line_length])


def is_one(start):
    new_line = []
    if start == line_length - 1:
        return True
    for j in range(5):
        if signal_line[j][start + 1] != '.':
            return False
    return True


def get_number(signal_: list):
    if signal_ == zero:
        return '0'
    if signal_ == two:
        return '2'
    if signal_ == three:
        return '3'
    if signal_ == four:
        return '4'
    if signal_ == five:
        return '5'
    if signal_ == six:
        return '6'
    if signal_ == seven:
        return '7'
    if signal_ == eight:
        return '8'
    if signal_ == nine:
        return '9'


i = 0
answer = ''
while i < line_length:
    if signal_line[0][i] == '#':
        if is_one(i):
            answer += '1'
            i += 2
        else:
            sig = []
            for j in range(5):
                sig.append(signal_line[j][i:i + 3])
            answer += get_number(sig)
            i += 3
    else:
        i += 1

print(answer)
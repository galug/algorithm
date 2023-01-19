import sys

size_input, n_input = map(str, sys.stdin.readline().split())
size = int(size_input)
_size = len(n_input)
vertical = 2 * size + 1
horizontal = size + 2


def make_one_right_vertical() -> str:
    one_vertical = ''
    for _ in range(horizontal - 1):
        one_vertical += ' '
    one_vertical += '|'
    return one_vertical + ' '


def make_one_left_vertical() -> str:
    one_vertical = '|'
    for _ in range(horizontal - 1):
        one_vertical += ' '
    return one_vertical + ' '


def make_two_vertical() -> str:
    two_vertical = '|'
    for _ in range(horizontal - 2):
        two_vertical += ' '
    return two_vertical + '|' + ' '


def make_horizontal() -> str:
    horizontal_ = ' '
    for _ in range(horizontal - 2):
        horizontal_ += '-'
    return horizontal_ + ' ' + ' '


def make_space() -> str:
    return ' ' * horizontal + ' '

# 맨 첫째 줄
answer = ''
for j in range(_size):
    if n_input[j] in '14':
        answer += make_space()
    else:
        answer += make_horizontal()
print(answer[:-1])


# 2번째
answer = ''
for _ in range(size):
    for i in range(_size):
        if n_input[i] in '123':
            answer += make_one_right_vertical()
        elif n_input[i] in '47890':
            answer += make_two_vertical()
        else:
            answer += make_one_left_vertical()
        if i == _size - 1:
            answer = answer[:-1]
    answer += '\n'
print(answer[:-1])
# 중간줄
answer = ''
for j in range(_size):
    if n_input[j] in '170':
        answer += make_space()
    else:
        answer += make_horizontal()
print(answer[:-1])
# 4번째
answer = ''
for _ in range(size):
    for i in range(_size):
        if n_input[i] in '134579':
            answer += make_one_right_vertical()
        elif n_input[i] in '2':
            answer += make_one_left_vertical()
        else:
            answer += make_two_vertical()
        if i == _size - 1:
            answer = answer[:-1]
    answer += '\n'
print(answer[:-1])
# 마지막줄
answer = ''
for j in range(_size):
    if n_input[j] in '147':
        answer += make_space()
    else:
        answer += make_horizontal()
print(answer[:-1], end = '')
# def make_both_vertical() -> str:
#     both_vertical = ''
#     for _ in range(size):
#         both_vertical += make_two_vertical()
#     return both_vertical

# def make_left_vertical():
#     left_vertical = ''
#     for _ in range(size):
#         left_vertical += make_one_left_vertical()
#     return left_vertical

# def make_right_vertical():
#     right_vertical = ''
#     for _ in range(size):
#         right_vertical += make_one_right_vertical()
#     return right_vertical

# one, two, three, four, five, six, seven, eight, nine, zero = '', '', '', '', '', '', '', '', '', ''
#
# # 1을 만든다.
# for i in range(3):
#     one += make_space()
#     if i == 2:
#         continue
#     one = make_right_vertical()
# # 2를 만든다.
# for i in range(3):
#     two += make_horizontal()
#     if i == 0:
#         two += make_right_vertical()
#     if i == 1:
#         two += make_left_vertical()
# # 3을 만든다.
# for i in range(3):
#     three += make_horizontal()
#     if i == 2:
#         break
#     three += make_right_vertical()
# # 4를 만든다.
# four += make_space()
# four += make_both_vertical()
# four += make_horizontal()
# four += make_right_vertical()
# four += make_space()
# # 5를 만든다.
# for i in range(3):
#     five += make_horizontal()
#     if i == 0:
#         five += make_left_vertical()
#     if i == 1:
#         five += make_right_vertical()
# # 6을 만든다.
# for i in range(3):
#     six += make_horizontal()
#     if i == 0:
#         six += make_left_vertical()
#     if i == 1:
#         six += make_both_vertical()
# # 7 을 만든다.
# for i in range(3):
#     seven += make_horizontal()
#     if i == 2:
#         continue
#     seven = make_right_vertical()
# # 8을 만든다.
# for i in range(3):
#     eight += make_horizontal()
#     if i == 2:
#         break
#     eight += make_both_vertical()
# # 9를 만든다.
# for i in range(3):
#     nine += make_horizontal()
#     if i == 0:
#         nine += make_both_vertical()
#     if i == 1:
#         nine += make_right_vertical()

# 구현형 문제
# 어셈블리어 코드를 기계어로 변환하는 코드
import sys

n = int(input())

opcode = ['ADD', 'SUB', 'MOV', 'AND', 'OR', 'NOT',
          'MULT', 'LSFTL', 'LSFTR', 'ASFTR', 'RL', 'RR']


def make_opcode(o: int) -> str:
    return '{0:04d}'.format(int(format(o, 'b')))

def make_octa_decimal(x: int) -> str:
    return '{0:03d}'.format(int(format(x, 'b')))


for _ in range(n):
    assembly_code = list(map(str, sys.stdin.readline().split()))
    answer = ''
    # opcode 부분 변환
    for i, op in enumerate(opcode):
        if op in assembly_code[0]:
            answer += make_opcode(i)
            if assembly_code[0][-1] == 'C':
                answer += '1'
            else:
                answer += '0'
            break
    # index : 5 변환
    answer += '0'
    # rD 변환
    answer += make_octa_decimal(int(assembly_code[1]))
    # rA 변환
    if (assembly_code[0] == 'NOT') or ('MOV' in assembly_code[0]):
        answer += '000'
    else:
        answer += make_octa_decimal(int(assembly_code[2]))
    # rB 변환
    rb = int(assembly_code[3])
    if assembly_code[0][-1] != 'C':
        answer += make_octa_decimal(rb)
        answer += '0'
    else:
        answer += make_opcode(rb)

    print(answer)

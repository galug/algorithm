# A는 매일 출근, B는 출근 다음날 무조건 쉬어야함, C는 출근한 다음날과 다다음날을 쉬어야함
# 이때 나올 수 있는 출근 기록
import sys

sys.setrecursionlimit(1000000000)

# 깊이 우선 탐색을 통한
def dfs(a, b, c, attendance_order: str):
    # 모든 출근을 조건에 맞게 기입할 수 있으면 정답을 반환
    if a == 0 and b == 0 and c == 0:
        global answer
        answer = attendance_order
        return True
    # a,b,c 의 개수가 같고 attendance_order[-1], attendance_order[-2] 가 같으면 뒤에 어떤 배열이 오더라도 상관없다.
    # 따라서 이미 방문한 곳으로 쳐도 무방하다. CBACBA 나 CABCBA 나 뒤에 어떤게 와도 상관없으므로 같다고 쳐도 됨
    if (a, b, c, attendance_order[-1], attendance_order[-2]) in dp:
        return
    # 방문 기록을 한다.
    dp.add((a, b, c, attendance_order[-1], attendance_order[-2]))
    # 조건에 맞춰서 깊이 우선 탐색을 한다.
    if c > 0:
        if len(attendance_order) >= 2 and attendance_order[-1] != 'C' and attendance_order[-2] != 'C':
            if dfs(a, b, c - 1, attendance_order + 'C'):
                return True
    if b > 0:
        if len(attendance_order) >= 1 and attendance_order[-1] != 'B':
            if dfs(a, b - 1, c, attendance_order + 'B'):
                return True
    if a > 0:
        if dfs(a - 1, b, c, attendance_order + 'A'):
            return True


# 출근 순서를 배열할 값을 입력 받고 개수를 센다.
arbitrary_array = list(map(str, sys.stdin.readline().rstrip()))
attendance_record = {'A': 0, 'B': 0, 'C': 0}
answer = ''
dp = set()

for ap in arbitrary_array:
    attendance_record[ap] += 1
# attendance_order[-1], attendance_order[-2] 가 항상 동작하게끔 'AA' 를 기본 값으로 넣어줌
if dfs(attendance_record['A'], attendance_record['B'], attendance_record['C'], 'AA'):
    # 맨 앞의 AA를 제외한 채로 출력
    print(answer[2:])
# 불가능하면 -1 을 출력
else:
    print(-1)

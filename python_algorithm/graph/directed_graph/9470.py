# 유향 그래프 심화 문제
import collections
import sys
# test_case 숫자
tc = int(input())
# 답안
answer = []
# test_case 숫자만큼 반복
for _ in range(tc):
    # tc_num, 노드 개수, 엣지 개수를 입력 받음
    tc_num, number_of_node, number_of_edge = map(int, sys.stdin.readline().split())
    # 들어오는 차수 개수 세기
    in_deed = [0] * (number_of_node + 1)
    # strahlers 순서 기록하기
    strahlers = [0] * (number_of_node + 1)
    # 들어온 strahlers 들을 기록한다.
    strahler_graph = [[] for _ in range(number_of_node + 1)]
    # 간선의 흐름을 기록
    graph = collections.defaultdict(list)
    # 들어오는 노드가 없는 노드들의 모임
    end_nodes = []
    # 모든 엣지들에 대한 계산
    for _ in range(number_of_edge):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        in_deed[end] += 1
    # 들어오는 노드가 없는 노드들을 기록, strahlers 에 1로 기록
    for i in range(1, number_of_node + 1):
        if in_deed[i] == 0:
            end_nodes.append(i)
            strahlers[i] = 1
    # 모든 노드를 꺼낸다.
    while end_nodes:
        # 들어오는 노드를 갱신하기 위한 배열
        new_end_nodes = []
        # 들어오는 노드가 없는 노드들을 반복으로 꺼냄
        for end_node in end_nodes:
            # in_deed 가 없는 노드들의 out_deed node 를 꺼냄
            while graph[end_node]:
                # out_deed 를 꺼냄
                destination = graph[end_node].pop()
                # out_deed의 strahler_graph 에 시작 부분의 strahler 를 집어넣음
                strahler_graph[destination].append(strahlers[end_node])
                in_deed[destination] -= 1
                # out_deed 의 노드에 진입 차수가 0일시
                if in_deed[destination] == 0:
                    strahler_graph[destination].sort(reverse=True)
                    # 조건에 따라 strahler 수를 정해준다.
                    if len(strahler_graph[destination]) > 1 and strahler_graph[destination][0] == strahler_graph[destination][1]:
                        strahlers[destination] = strahler_graph[destination][0] + 1
                    else:
                        strahlers[destination] = strahler_graph[destination][0]
                    # 진입 차수가 없는 노드로 추가
                    new_end_nodes.append(destination)
        # 진입 차수가 없는 노드들을 갱신
        end_nodes = new_end_nodes
    # 가장 큰 수가 대표 strahler 가 된다.
    answer.append([tc_num, max(strahlers)])

for tc_num, a in answer:
    print(tc_num, a)

import collections
import heapq
import sys

# 도시의 수
n = int(input())
# 버스의 수
m = int(input())

# 그래프를 저장하는 과정
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append([end, weight])

# 시작점과 끝점
start, end = map(int,sys.stdin.readline().split())

# 다익스트라 알고리즘을 위한 준비
dist = [float('inf')]*(n+1)
heap = [[0, start]]
dist[start] = 0

# 다익스트라 알고리즘
while heap:
    weight, destination = heapq.heappop(heap)
    # 도착지에 원래 도달할 수 있는 비용이 원래 가는 길의 비용보다 적으면 그 길을 갈 가치가 없다.
    if dist[destination] < weight:
        continue
    if destination == end:
        break
    # 그래프에서 다른 곳으로 가는 길을 뽑아냄
    for new_destination, new_weight in graph[destination]:
        # temp = start-> destination(weight) + destination -> new_destination(weight)
        temp = new_weight + dist[destination]
        # 기존에 목적지에 도착하는 방법보다 더 적은 비용으로 갈 수 있을 시 heap에 추가
        if temp < dist[new_destination]:
            dist[new_destination] = temp
            heapq.heappush(heap, [temp, new_destination])

print(dist[end])

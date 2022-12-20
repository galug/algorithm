import collections

s = int(input())

que = collections.deque([[1, 0, 0]])
visited = set()
while que:
    screen, clipboard, time = que.popleft()
    if (screen, clipboard) in visited:
        continue
    if screen == s:
        print(time)
        break
    visited.add((screen, clipboard))
    que.append([screen, screen, time + 1])
    if screen - 1 > 1:
        que.append([screen - 1, clipboard, time + 1])
    if clipboard != 0:
        que.append([screen + clipboard, clipboard, time + 1])

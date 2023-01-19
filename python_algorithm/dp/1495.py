# 기타리스트
# 각 volume_list 만큼 더하거나 빼주면서 마지막에 가장 큰 수가 나오게끔하자.
import sys
# 입력값 받기
number_of_music, volume, max_volume = map(int, sys.stdin.readline().split())
volume_list = list(map(int, sys.stdin.readline().split()))

# solution 함수
def solution() -> int:
    # 미리 volume 을 set()로 받아 놓는다.
    prev_volumes = {volume}
    for volume_idx in range(number_of_music):
        cur_volumes = set()
        if len(prev_volumes) == 0:
            return -1
        while prev_volumes:
            v = prev_volumes.pop()
            if v + volume_list[volume_idx] <= max_volume:
                cur_volumes.add(v + volume_list[volume_idx])
            if v - volume_list[volume_idx] >= 0:
                cur_volumes.add(v - volume_list[volume_idx])
        prev_volumes |= cur_volumes
    if len(prev_volumes) == 0:
        return -1
    else:
        return max(prev_volumes)


print(solution())

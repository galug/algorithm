import sys

h, w = map(int,sys.stdin.readline().split())
blocks = list(map(int,sys.stdin.readline().split()))

left, right = 0, w - 1
left_max, right_max = blocks[0], blocks[w-1]
total_water = 0

while left <= right:
    if left_max < right_max:
        if left_max >= blocks[left]:
            total_water += (left_max-blocks[left])
        else:
            left_max = max(left_max, blocks[left])
        left += 1
    else:
        if right_max >= blocks[right]:
            total_water += (right_max-blocks[right])
        else:
            right_max = max(right_max, blocks[right])
        right -= 1

print(total_water)
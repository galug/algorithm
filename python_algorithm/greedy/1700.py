import sys

n, k = map(int, sys.stdin.readline().split())
electrical_appliances = list(map(int, sys.stdin.readline().split()))


def multi_schedule():
    if n > k:
        return 0
    pluged_tab = set()
    answer = 0
    for i in range(k):
        if electrical_appliances[i] in pluged_tab:
            continue
        if len(pluged_tab) < n:
            pluged_tab.add(electrical_appliances[i])
        else:
            not_plug = set()
            for j in range(i + 1, k):
                if len(not_plug) == n-1:
                    break
                if electrical_appliances[j] in pluged_tab:
                    not_plug.add(electrical_appliances[j])
            pluged_tab.remove((pluged_tab - not_plug).pop())
            pluged_tab.add(electrical_appliances[i])
            answer += 1
    return answer
print(multi_schedule())

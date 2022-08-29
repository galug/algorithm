def dailyTemperatures(temperatures: [int]) -> [int]:
    stack = []
    t_list = [0]*len(temperatures)
    for i, t in enumerate(temperatures):
        while stack and stack[-1][1] < t:
            t_list[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append([i,t])
    return t_list
t = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(t))
import collections


def findItinerary(tickets: [[str]]) -> [str]:
    graph = collections.defaultdict(list)
    for f, t in sorted(tickets):
        graph[f].append(t)
    results = []

    def dfs(start):
        while graph[start]:
            dfs(graph[start].pop(0))
        results.append(start)

    dfs("JFK")
    return results[::-1]

print([[1,2],[2,3]][1>2])
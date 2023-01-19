import sys


def print_dp():
    for i in range(number_of_chapter):
        for j in range(number_of_chapter):
            print(dp[i][j])
        print()


def dfs(start: int, end: int):
    if start == end:
        return dp[start][start]
    if start == end - 1:
        return dp[start][end]
    for middle in range(start, end):
        dp[start][end] = min(dp[start][end],
                             dfs(start, middle) + dfs(middle + 1, end) + sum_of_chapters[end + 1] - sum_of_chapters[
                                 start])
    return dp[start][end]


tc = int(input())
for _ in range(tc):
    number_of_chapter = int(sys.stdin.readline())
    chapters = list(map(int, sys.stdin.readline().split()))
    answer = sys.maxsize
    sum_of_chapters = [0, chapters[0]]
    dp = [[sys.maxsize] * number_of_chapter for _ in range(number_of_chapter)]
    for i in range(0, number_of_chapter - 1):
        dp[i][i] = chapters[i]
        dp[i][i + 1] = chapters[i] + chapters[i + 1]
        sum_of_chapters.append(sum_of_chapters[i + 1] + chapters[i + 1])
    dp[-1][-1] = chapters[-1]
    print(sum_of_chapters)
    print(dfs(0, number_of_chapter - 1))
    for _ in range(number_of_chapter):
        print(dp[_])

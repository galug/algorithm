class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        stack = []
        num_of_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num_of_island += 1
                    stack.append([i, j])
                    while stack:
                        y, x = stack.pop()
                        grid[y][x] = '0'
                        if y + 1 < len(grid) and grid[y + 1][x] == '1': stack.append([y + 1, x])
                        if y - 1 >= 0 and grid[y - 1][x] == '1': stack.append([y - 1, x])
                        if x + 1 < len(grid[i]) and grid[y][x + 1] == '1': stack.append([y, x + 1])
                        if x - 1 >= 0 and grid[y][x - 1] == '1': stack.append([y, x - 1])
        return num_of_island


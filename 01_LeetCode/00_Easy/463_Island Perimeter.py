def island_perimeter(grid: list) -> int:
    # rows = len(grid)
    # cols = len(grid[0])
    # perimeter = 0
    # neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #
    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 1:
    #             for r, c in neighbours:
    #                 nr, nc = row + r, col + c
    #                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
    #                     perimeter += 1
    #                 elif not (0 <= nr < rows and 0 <= nc < cols):
    #                     perimeter += 1
    #
    # return perimeter
    r, c, s = len(grid), len(grid[0]), 0
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                s += 4
                if i and grid[i - 1][j]:
                    s -= 2
                if j and grid[i][j - 1]:
                    s -= 2
    return s

grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(island_perimeter(grid1))
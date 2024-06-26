#!/usr/bin/python3

def island_perimeter(grid):
    col = range(len(grid))
    row = range(len(grid[0]))
    perimeter = 0
    for i in col:
        for j in row:
            if grid[i][j] == 1:
                if grid[i-1][j] == 0 or i == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                if grid[i][j-1] == 0 or j == 0:
                    perimeter += 1
                if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter

from typing import List
import matplotlib.pyplot as plt
import random

def generate_random_grid(rows, cols, density=0.3):
    grid = [[1 if random.random() < density else 0 for _ in range(cols)] for _ in range(rows)]
    return grid

class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        counter = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 1: 
                    counter += 1
                    self.check(grid, r, c)
                    self.display_grid(grid, f"Island {counter}", pause_time=0.1)

        return counter

    def check(self, grid: List[List[int]], r, c):
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == 0:
            return
        grid[r][c] = 0 
        self.check(grid, r - 1, c)
        self.check(grid, r, c + 1)
        self.check(grid, r + 1, c)
        self.check(grid, r, c - 1)

    def display_grid(self, grid, title, pause_time=2):
        plt.imshow(grid, cmap='viridis', interpolation='none')
        plt.title(title)
        plt.pause(pause_time)
        plt.clf()

grid = generate_random_grid(30, 30, density=0.5)

solution = Solution()
result = solution.numIslands(grid)
print(result)

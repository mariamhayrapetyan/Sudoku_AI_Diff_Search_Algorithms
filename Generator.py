from random import shuffle, randrange
import copy


class SudokuGenerator:

    def __init__(self, level):
        self.counter = 0
        self._level = level
        self.grid_copy = []
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.generate_grid()


    def generate_grid(self):
        self.generate_solution(self.grid)
        g = self.remove_numbers(self._level, self.grid)
        return g


    def valid(self, grid, row, col, num):
        #checking by row
        if num in grid[row]:
            return False

        # checking by column
        for i in range(9):
            if grid[i][col] == num:
                return False

        # checking by subgrid
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(subgrid_row, (subgrid_row + 3)):
            for j in range(subgrid_col, (subgrid_col + 3)):
                if grid[i][j] == num:
                    return False
        return True

    def find_empty_square(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i,j)
        return

    def solve(self, grid):
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if self.valid(grid, row, col, num):
                        grid[row][col] = num
                        if not self.find_empty_square(grid):
                            self.counter += 1
                            break
                        else:
                            if self.solve(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def generate_solution(self, grid):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                shuffle(numbers)
                for num in numbers:
                    if self.valid(grid, row, col, num):
                        grid[row][col] = num
                        if not self.find_empty_square(grid):
                            return True
                        else:
                            if self.generate_solution(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def find_non_empty_squares(self, grid):
        non_empty = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    non_empty.append((i, j))
        shuffle(non_empty)
        return non_empty

    def remove_numbers(self, level, grid):
        non_empty = self.find_non_empty_squares(grid)
        non_empty_count = len(non_empty)
        limit = 3

        if level == "Easy":
            val = randrange(45, 53)
        if level == "Medium":
            val = randrange(36, 44)
        if level == "Hard":
            val = randrange(27, 35)

        while limit > 0 and non_empty_count >= 22:
            row, col = non_empty.pop()
            non_empty_count -= 1
            removed = grid[row][col]
            grid[row][col] = 0
            grid_copy = copy.deepcopy(grid)
            self.counter = 0
            self.solve(grid_copy)
            if self.counter != 1:
                grid[row][col] = removed
                non_empty_count += 1
                limit -= 1
            elif non_empty_count == val:
                return grid
        if non_empty_count != val:
            if level == "Easy":
                if 45 <= non_empty_count <= 53:
                    return grid
                else:
                    return self.remove_numbers(level, grid_copy)
            if level == "Medium":
                if 36 <= non_empty_count <= 44:
                    return grid
                else:
                    return self.remove_numbers(level, grid_copy)
            if level == "Hard":
                if 27 <= non_empty_count <= 35:
                    return grid
                else:
                    return self.remove_numbers(level, grid_copy)


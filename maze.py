import random
import time

from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = seed

        if seed is not None:
            random.seed(seed)

        self.__cells = []
        self.__create_cells()

        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                col_cells.append(cell)

            self.__cells.append(col_cells)

        # draw all cells after creation
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]

        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        cell.draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is not None:
            self.__win.redraw()
            time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):

        while True:

            left = (i - 1, j)
            right = (i + 1, j)
            up = (i, j - 1)
            down = (i, j + 1)

            self.__cells[i][j].visited = True

            to_visit = []

            if i > 0 and self.__cells[i - 1][j].visited is False:
                to_visit.append(left)
            if i < self.__num_cols - 1 and self.__cells[i + 1][j].visited is False:
                to_visit.append(right)
            if j > 0 and self.__cells[i][j - 1].visited is False:
                to_visit.append(up)
            if j < self.__num_rows - 1 and self.__cells[i][j + 1].visited is False:
                to_visit.append(down)

            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return

            choice_index = random.randrange(len(to_visit))
            new_i, new_j = to_visit[choice_index]

            new_cell = (new_i, new_j)

            if new_cell == left:
                self.__cells[i][j].has_left_wall = False
                self.__cells[new_i][new_j].has_right_wall = False

            if new_cell == right:
                self.__cells[i][j].has_right_wall = False
                self.__cells[new_i][new_j].has_left_wall = False

            if new_cell == up:
                self.__cells[i][j].has_top_wall = False
                self.__cells[new_i][new_j].has_bottom_wall = False

            if new_cell == down:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[new_i][new_j].has_top_wall = False

            self.__break_walls_r(new_i, new_j)

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def _solve_r(self, i, j):

        self.__animate()
        current_cell = self.__cells[i][j]
        current_cell.visited = True

        if (i, j) == (self.__num_cols - 1, self.__num_rows - 1):
            return True

        # left

        if (
            i > 0
            and not current_cell.has_left_wall
            and self.__cells[i - 1][j].visited is False
        ):
            target_cell = self.__cells[i - 1][j]
            current_cell.draw_move(target_cell)
            if self._solve_r(i - 1, j):
                return True
            else:
                current_cell.draw_move(target_cell, undo=True)

        # right

        if (
            i < self.__num_cols - 1
            and not current_cell.has_right_wall
            and self.__cells[i + 1][j].visited is False
        ):
            target_cell = self.__cells[i + 1][j]
            current_cell.draw_move(target_cell)
            if self._solve_r(i + 1, j):
                return True
            else:
                current_cell.draw_move(target_cell, undo=True)

        # up

        if (
            j > 0
            and not current_cell.has_top_wall
            and self.__cells[i][j - 1].visited is False
        ):
            target_cell = self.__cells[i][j - 1]
            current_cell.draw_move(target_cell)
            if self._solve_r(i, j - 1):
                return True
            else:
                current_cell.draw_move(target_cell, undo=True)

        # down

        if (
            j < self.__num_rows - 1
            and not current_cell.has_bottom_wall
            and self.__cells[i][j + 1].visited is False
        ):
            target_cell = self.__cells[i][j + 1]
            current_cell.draw_move(target_cell)
            if self._solve_r(i, j + 1):
                return True
            else:
                current_cell.draw_move(target_cell, undo=True)
        return False

    def solve(self):
        return self._solve_r(0, 0)

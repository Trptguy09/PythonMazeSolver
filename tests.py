import unittest

from cell import Cell
from maze import Maze


class TestCell(unittest.TestCase):

    def test_initial_state(self):
        cell = Cell()

        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)
        self.assertFalse(cell.visited)

    def test_draw_sets_coordinates(self):
        cell = Cell()

        cell.draw(0, 0, 10, 20)

        self.assertEqual(cell._Cell__x1, 0)
        self.assertEqual(cell._Cell__y1, 0)
        self.assertEqual(cell._Cell__x2, 10)
        self.assertEqual(cell._Cell__y2, 20)

    def test_get_center_returns_correct_point(self):
        cell = Cell()
        cell.draw(0, 0, 10, 20)

        center = cell.get_center()

        self.assertEqual(center.x, 5)
        self.assertEqual(center.y, 10)

    def test_draw_no_window(self):
        cell = Cell(win=None)

        try:
            cell.draw(0, 0, 10, 10)
        except Exception as e:
            self.fail(f"draw() raised exception: {e}")

    def test_draw_move_no_window(self):
        cell1 = Cell()
        cell2 = Cell()

        cell1.draw(0, 0, 10, 10)
        cell2.draw(10, 0, 20, 10)

        try:
            cell1.draw_move(cell2)
            cell1.draw_move(cell2, undo=True)
        except Exception as e:
            self.fail(f"draw_move() raised exception: {e}")

    def test_draw_move_centers(self):
        cell1 = Cell()
        cell2 = Cell()

        cell1.draw(0, 0, 10, 10)
        cell2.draw(10, 10, 20, 20)

        c1 = cell1.get_center()
        c2 = cell2.get_center()

        self.assertEqual(c1.x, 5)
        self.assertEqual(c1.y, 5)
        self.assertEqual(c2.x, 15)
        self.assertEqual(c2.y, 15)


class TestMaze(unittest.TestCase):

    def test_maze_initialization_creates_correct_grid(self):
        maze = Maze(0, 0, 3, 4, 10, 10, win=None, seed=1)
        cells = maze._Maze__cells

        self.assertEqual(len(cells), 4)
        self.assertEqual(len(cells[0]), 3)

    def test_entrance_and_exit_are_open(self):
        maze = Maze(0, 0, 3, 3, 10, 10, win=None, seed=1)
        cells = maze._Maze__cells

        self.assertFalse(cells[0][0].has_top_wall)
        self.assertFalse(cells[2][2].has_bottom_wall)

    def test_cells_exist(self):
        maze = Maze(0, 0, 2, 2, 10, 10, win=None, seed=1)
        cells = maze._Maze__cells

        for i in range(2):
            for j in range(2):
                self.assertIsNotNone(cells[i][j])

    def test_cells_visited_reset(self):
        maze = Maze(0, 0, 3, 3, 10, 10, win=None, seed=1)
        cells = maze._Maze__cells

        for i in range(3):
            for j in range(3):
                self.assertFalse(cells[i][j].visited)

    def test_maze_has_removed_walls(self):
        maze = Maze(0, 0, 3, 3, 10, 10, win=None, seed=1)
        cells = maze._Maze__cells

        removed_wall_found = False

        for i in range(3):
            for j in range(3):
                cell = cells[i][j]
                if (
                    not cell.has_top_wall
                    or not cell.has_bottom_wall
                    or not cell.has_left_wall
                    or not cell.has_right_wall
                ):
                    removed_wall_found = True

        self.assertTrue(removed_wall_found)


if __name__ == "__main__":
    unittest.main()

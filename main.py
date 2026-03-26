from graphics import Window
from maze import Maze


def main():
    # set window size
    win = Window(1000, 1000)
    maze = Maze(100, 100, 25, 25, 32, 32, win)  # 800 ratio leaves border
    maze.solve()
    win.wait_for_close()


main()

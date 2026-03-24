from graphics import Window
from maze import Maze


def main():
    # set window size
    win = Window(1000, 1000)
    maze = Maze(100, 100, 16, 16, 50, 50, win)

    win.wait_for_close()


main()

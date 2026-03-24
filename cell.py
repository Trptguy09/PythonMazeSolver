from graphics import Line, Point


class Cell:
    def __init__(self, Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = Window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:

            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            left_wall = Line(p1, p2)
            self.__win.draw_line(left_wall, "blue")

        if self.has_right_wall:

            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            right_wall = Line(p1, p2)
            self.__win.draw_line(right_wall, "blue")

        if self.has_top_wall:

            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            top_wall = Line(p1, p2)
            self.__win.draw_line(top_wall, "blue")

        if self.has_bottom_wall:

            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            bottom_wall = Line(p1, p2)
            self.__win.draw_line(bottom_wall, "blue")

    def get_center(self):
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):

        current_center = self.get_center()
        target_center = to_cell.get_center()

        line = Line(current_center, target_center)

        line_color = "gray" if undo else "red"

        if self.__win is not None:
            self.__win.draw_line(line, line_color)

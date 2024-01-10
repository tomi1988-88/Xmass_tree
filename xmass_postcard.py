from typing import Union, List
from xmass_trees import TreeObj


class Postcard:
    def __init__(self, cols: int = 50, rows: int = 30) -> None:
        self.cols = cols
        self.rows = rows
        self.array = [[" " for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.cols):
            self.array[0][i] = "-"
            self.array[-1][i] = "-"

        for i in range(1, self.rows - 1):
            self.array[i][0] = "|"
            self.array[i][-1] = "|"

    def place(self, obj: Union[TreeObj, str], y: int = 0, x: int = 0):
        if isinstance(obj, TreeObj):
            y = obj.y
            x = obj.x - obj.first_row_len + 1

            list_to_place = obj.tree_list
            self.__place(list_to_place, y, x)
            return self

        elif isinstance(obj, str):
            y = y
            x = x + 1

            list_of_lines = obj.split("\n")
            list_to_place = [list(line) for line in list_of_lines]

            self.__place(list_to_place, y, x)
            return self

    def __place(self, list_to_place: List[List], y: int, x: int):
        for line in list_to_place:

            x_ = x  # At the beginning of every line we have to go back to the initial column

            if y > self.rows:
                break
            elif y < 1:
                y += 1
                continue

            for char in line:
                if x_ >= self.cols:
                    break
                elif x_ < 1:
                    x_ += 1
                    continue

                if char != " ":
                    self.array[y][x_] = char
                x_ += 1
            y += 1

    def __str__(self):
        return "\n".join(["".join(line) for line in self.array])

    def __repr__(self):
        return f"Postcard({self.cols}, {self.rows})"

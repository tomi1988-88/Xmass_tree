from xmass_funcs import replace_with_interval


def tree_1(lines: int) -> str:
    stars = 1
    spaces = lines - 1  # Because a line starts with index 0.

    tree_str = str()

    while spaces >= 0:
        tree_str += f"{' ' * spaces}{'*' * stars}\n"
        stars += 2
        spaces -= 1

    return tree_str[:-1]  # In order to omit last new line character


def tree_2(lines: int) -> str:
    stars = 1
    spaces = lines

    tree_str = f"{' ' * (lines - 1)}X\n" + f"{' ' * (lines - 1)}^\n"

    while spaces > 1:
        tree_str += f"{' ' * (spaces - 2)}/{'*' * stars}\\\n"
        stars += 2
        spaces -= 1

    tree_str += f"{' ' * (lines - 2)}| |"

    return tree_str


def tree_3(lines: int, interval: int) -> str:
    stars = 1
    spaces = lines

    tree_str = f"{' ' * (lines - 1)}X\n" + f"{' ' * (lines - 1)}^\n" + f"{' ' * (spaces - 2)}/*\\\n"

    while spaces > 2:
        tree_str += f"{' ' * (spaces - 3)}/{'*$' * stars}*\\\n"
        stars += 1
        spaces -= 1

    tree_str += f"{' ' * (lines - 2)}| |"

    tree_str = replace_with_interval(tree_str, interval)

    return tree_str


class TreeObj:
    def __init__(self, index: int, lines: int, interval: int, y: int, x: int) -> None:
        self.index = index
        self.lines = lines
        self.interval = interval
        self.y = y
        self.x = x

    @property
    def tree_raw(self):
        return tree_3(self.lines, self.interval)

    @property
    def tree_list(self):
        return [list(line) for line in self.tree_raw.split("\n")]

    @property
    def first_row_len(self):
        return len(self.tree_list[0])

    def __str__(self):
        return self.tree_raw

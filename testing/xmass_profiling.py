import cProfile
import timeit
from xmass_trees import tree_1
from xmass_trees import tree_2
from xmass_trees import tree_3
from xmass_trees import TreeObj
from xmass_funcs import replace_with_interval


def tree_1_lst(lines: int) -> str:
    """Simplest tree"""
    stars = 1
    spaces = lines - 1  # Because a line starts with index 0.

    tree_lst = list()

    while spaces >= 0:
        tree_lst.extend([" " for _ in range(spaces)] + ["*" for _ in range(stars)] + ["\n"])

        stars += 2
        spaces -= 1

    return "".join(tree_lst[:-1])


def replace_with_interval_str_cut(tree_str: str, interval: int) -> str:
    if interval == 1:
        return tree_str  # changed tree_str.replace("$", "O")

    num_of_dec = tree_str.count("O")  # changed "$"

    # Altered part to the end:
    result = ""
    temp = tree_str

    for i in range(1, num_of_dec + 1):
        ind_O = temp.find("O") + 1
        if i % interval == 1:
            result += temp[:ind_O]
            temp = temp[ind_O:]
        else:
            result += temp[:ind_O - 1] + "*"
            temp = temp[ind_O:]

    result += temp

    return result


def tree_3_str_cut(lines: int, interval: int) -> str:
    stars = 1
    spaces = lines

    tree_str = f"{' ' * (lines - 1)}X\n" + f"{' ' * (lines - 1)}^\n" + f"{' ' * (spaces - 2)}/*\\\n"

    while spaces > 2:
        tree_str += f"{' ' * (spaces - 3)}/{'*O' * stars}*\\\n"  # changed {'*$' * stars} to {'*O' * stars}
        stars += 1
        spaces -= 1

    tree_str += f"{' ' * (lines - 2)}| |"

    tree_str = replace_with_interval_str_cut(tree_str, interval)  # changed replace_with_interval to replace_with_interval_amend

    return tree_str


cProfile.run("tree_1(5)")
print(timeit.repeat("tree_1(5)", repeat=3, globals=globals()))

cProfile.run("tree_1_lst(5)")
print(timeit.repeat("tree_1_lst(5)", repeat=3, globals=globals()))

cProfile.run("tree_2(5)")
print(timeit.repeat("tree_2(5)", repeat=3, globals=globals()))

cProfile.run("tree_3(5, 1)")
print(timeit.repeat("tree_3(5, 1)", repeat=3, globals=globals()))

cProfile.run("tree_3(5, 3)")
print(timeit.repeat("tree_3(5, 3)", repeat=3, globals=globals()))

cProfile.run("tree_3_amend(5, 3)")
print(timeit.repeat("tree_3_amend(5, 3)", repeat=3, globals=globals()))

cProfile.run("TreeObj(1, 5, 1, 1, 1).tree_raw")
print(timeit.repeat("TreeObj(1, 5, 1, 1, 1).tree_raw", repeat=3, globals=globals()))

cProfile.run("TreeObj(1, 5, 3, 1, 1).tree_raw")
print(timeit.repeat("TreeObj(1, 5, 3, 1, 1).tree_raw", repeat=3, globals=globals()))

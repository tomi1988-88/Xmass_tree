import cProfile
import timeit
from Xmass_tree import tree_1
from Xmass_tree import tree_2
from Xmass_tree import tree_3
from Xmass_tree import TreeObj


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

# print(tree_1(5))
# print(tree_1_lst(5))


# cProfile.run("tree_1(5)")
# cProfile.run("tree_1_lst(5)")
# cProfile.run("tree_2(5)")
# cProfile.run("tree_3(5, 1)")
# cProfile.run("tree_3(5, 3)")
cProfile.run("TreeObj(1, 5, 1, 1, 1).tree_raw")
cProfile.run("TreeObj(1, 5, 3, 1, 1).tree_raw")


# print(globals())
# print(locals())
# print(timeit.repeat("tree_1(5)", repeat=3, globals=globals()))
# print(timeit.repeat("tree_1_lst(5)", repeat=3, globals=globals()))

# print(timeit.repeat("tree_2(5)", repeat=3, globals=globals()))
# print(timeit.repeat("tree_3(5, 1)", repeat=3, globals=globals()))
# print(timeit.repeat("tree_3(5, 3)", repeat=3, globals=globals()))
# print(timeit.repeat("TreeObj(1, 5, 1, 1, 1).tree_raw", repeat=3, globals=globals()))
print(timeit.repeat("TreeObj(1, 5, 3, 1, 1).tree_raw", repeat=3, globals=globals()))


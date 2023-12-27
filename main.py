import sys
from xmass_exceptions import (TooSmallTreeException,
                              TooSmallIntervalException)
from xmass_trees import (tree_1,
                         tree_2,
                         tree_3,
                         TreeObj)
from xmass_postcard import Postcard

# STAGE 1 & 2 - RUN
if __name__ == "__main__":
    user_input = input()

    try:
        lines = int(user_input)
        if lines < 2:
            raise TooSmallTreeException(lines)
    except ValueError as e:
        sys.exit(e)
    except TooSmallTreeException as e:
        sys.exit(e)

    print(tree_1(lines))
    print(tree_2(lines))

# # STAGE 3 - RUN
# if __name__ == "__main__":
#     user_input = input()
#
#     try:
#         lines, interval = user_input.split()
#     except ValueError as e:
#         sys.exit(f"{e} - input format: lines interval; your input: {user_input}")
#
#     try:
#         lines = int(lines)
#         interval = int(interval)
#         if lines < 2:
#             raise TooSmallTreeException(lines)
#         if interval < 1:
#             raise TooSmallIntervalException(interval)
#     except ValueError as e:
#         sys.exit(f"{e} - line and interval must be integers. Your input {user_input}")
#     except TooSmallTreeException as e:
#         sys.exit(e)
#
#     print(tree_3(lines, interval))


# Stage 4 - RUN
if __name__ == "__main__":
    user_input = input()

    user_input = user_input.split()

    if len(user_input) == 2:

        lines, interval = user_input

        try:
            lines = int(lines)
            interval = int(interval)
            if lines < 2:
                raise TooSmallTreeException(lines)
            if interval < 1:
                raise TooSmallIntervalException(interval)
        except ValueError as e:
            sys.exit(f"{e} - line and interval must be integers. Your input {user_input}")
        except TooSmallTreeException as e:
            sys.exit(e)

        print(tree_3(lines, interval))
        sys.exit(0)

    if len(user_input) % 4 != 0:
        sys.exit(
            "Wrong number of args! To generate simple tree 2 ints are enough. To generate postcard at least 4 ints are needed (or more but it must be multiplication of 4)")

    try:
        user_input = [int(x) for x in user_input]
    except ValueError as e:
        sys.exit(f"{e} - all args must be integers. Your input {user_input}")

    trees_data = [user_input[i:i + 4] for i in range(0, len(user_input), 4)]

    trees = []

    for index, [lines, interval, y, x] in enumerate(trees_data, start=1):
        try:
            if lines < 2:
                raise TooSmallTreeException(lines)
            if interval < 1:
                raise TooSmallIntervalException(interval)
        except ValueError as e:
            sys.exit(f"{e} - line and interval must be integers. Wrong input in tree number {index}")
        except TooSmallTreeException as e:
            sys.exit(f"{e} - Wrong input in tree number {index}")

        temp = TreeObj(index, lines, interval, y, x)
        trees.append(TreeObj(index, lines, interval, y, x))

    postcard = Postcard()
    postcard.place("Merry Xmas", 27, 19)

    for tree in trees:
        postcard.place(tree)

    print(postcard)

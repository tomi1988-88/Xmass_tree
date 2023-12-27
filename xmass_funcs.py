def replace_with_interval(tree_str: str, interval: int) -> str:

    if interval == 1:
        return tree_str.replace("$", "O")

    num_of_dec = tree_str.count("$")

    for i in range(1, num_of_dec + 1):
        if i % interval == 1:
            tree_str = tree_str.replace("$", "O", 1)
        else:
            tree_str = tree_str.replace("$", "*", 1)

    return tree_str

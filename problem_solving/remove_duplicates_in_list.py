def remove_duplicates(my_list):
    """
    Use a set to remove the duplicates. Insertion order isn't preserved.
    :param my_list:
    :return:
    """
    return set(my_list)


def remove_dup(my_list: list):
    """
    Use a set to track the visited elements
    Loop through the input list and if the current element isn't visited, add it to another list
    :param my_list:
    :return:
    """
    visited = set()
    unique_ele = []
    for no in my_list:
        if no not in visited:
            unique_ele.append(no)
        visited.add(no)
    return unique_ele


if __name__ == '__main__':
    inp = [1, 10, 1, 2, 2, 3, 10, 3, 3, 4, 5, 5]
    # print(remove_duplicates(inp))
    print(remove_dup(inp))

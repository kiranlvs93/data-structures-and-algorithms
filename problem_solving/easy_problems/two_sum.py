array = [3, 5, -4, 8, 11, 1, -1, 6]
target_sum = 10


def two_sum_brute_force():
    """
    O(n^2) time complexity / O(1) space complexity
    :return:
    """
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]


def two_sum_hash_table_technique():
    """
    O(n) time complexity / O(n) space complexity
    :return:
    """
    table = []
    for x in array:
        if (y := target_sum - x) in table:
            return [x, y]
        else:
            table.append(x)
    return []


def two_sum_window_technique():
    """
    O(nlogn) time complexity / O(1) space complexity
    :return:
    """
    array.sort()
    lp, rp = 0, len(array) - 1
    while lp < rp:
        sum_ = array[lp] + array[rp]
        if sum_ == target_sum:
            return [array[lp], array[rp]]
        elif sum_ > target_sum:
            rp -= 1
        else:
            lp += 1
    return []


print(two_sum_brute_force())
print(two_sum_hash_table_technique())
print(two_sum_window_technique())

from decorators.decorators_util import print_inp_op


@print_inp_op
def sub_array_sum_v3(arr, k):
    """
    Approach- 3 (without space)
    Instead of considering all the start and end points and then finding the sum for each subarray corresponding to those points, we can directly find the sum on the go while considering different end points. \
    i.e. We can choose a particular start point and while iterating over the end points, we can add the element corresponding to the end point to the sum formed till now. Whenever the sum equals the required kk value, we can update the countcount value.

    We do so while iterating over all the end indices possible for every start index. Whenever, we update the start index, we need to reset the sum value to 0
    :param arr:
    :param k:
    :return:
    """
    start = count = 0
    n = len(arr)
    while start < n:
        sa_sum = 0
        end = start
        while end < n:
            sa_sum += arr[end]
            end += 1
            if sa_sum == k:
                count += 1
        start += 1
    return count


# sub_array_sum_v3([1, 0, 1], 1)
# sub_array_sum_v3([0, 0, 0], 0)


@print_inp_op
def sub_array_sum_v4(arr, k):
    """
    Using Hashmap
    If the cumulative sum(represented by sum[i] for sum up to i^{th} index) up to two indices is the same,
    the sum of the elements lying in between those indices is zero. Extending the same thought further, if the
    cumulative sum up to two indices, say i and j is at a difference of k i.e. if sum[i] - sum[j] = k,
    the sum of elements lying between indices i and j is k.

    Time complexity : O(n)
    Space complexity : O(n)
    :param arr:
    :param k:
    :return:
    """
    pfs = [arr[0]]

    for i in range(1, len(arr)):
        pfs.append(arr[i] + pfs[i - 1])

    pfs_freq = {0: 1}
    count = 0
    for s in pfs:
        if (s - k) in pfs_freq:
            count += pfs_freq[s - k]
        pfs_freq[s] = 1 + pfs_freq.get(s, 0)
    return count


sub_array_sum_v4([1, 0, 1], 1)
sub_array_sum_v4([0, 0, 0], 0)

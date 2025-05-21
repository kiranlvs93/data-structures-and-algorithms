"""

"""

from decorators.decorators_util import print_inp_op


@print_inp_op
def get_sqrt_of_num(num):
    start = 2
    end = num
    if num < 2:
        return num

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == num:
            return mid
        elif mid * mid > num:
            end = mid - 1
        elif mid * mid < num:
            start = mid + 1
    return end


# get_sqrt_of_num(8)


@print_inp_op
def get_sqrt_of_num_ver2(num):
    start = 2
    end = num
    if num < 2:
        return num

    while start <= end:
        mid = (start + end) // 2
        #  All integers**2 <=num are possible square roots
        if mid * mid <= num:
            # Moving the boundaries to next element if the next element can also be a square root
            if (mid + 1) * (mid + 1) <= num:
                start = mid + 1
            else:
                return mid
        else:
            end = mid - 1


get_sqrt_of_num_ver2(8)

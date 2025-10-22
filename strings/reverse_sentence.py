from decorators.decorators_util import print_inp_op


@print_inp_op
def reverse_sentence(inp: str):
    """
    TC = O(N2), SC = O(N)
    :param inp:
    :return:
    """
    output = []
    for word in inp.split(" "):
        if word != '':
            output.insert(0, word)  # this is the O(N2) operation
    return " ".join(output)


reverse_sentence("the   sky is blue   ")


@print_inp_op
def reverse_sentence_optimized(inp: str):
    """
    TC = O(N), SC = O(N)
    :param inp:
    :return:
    """
    output = []
    for word in inp.split(" "):
        if word != '':
            output.append(word)  # this is the O(N2) operation
    return " ".join(output[::-1])


reverse_sentence_optimized("the   sky is blue   ")


@print_inp_op
def reverse_sentence_optimized_pythonic(inp: str):
    """
    TC = O(N), SC = O(N)
    :param inp:
    :return:
    """
    return " ".join([word for word in inp.split() if word != ''][::-1])

reverse_sentence_optimized_pythonic("the   sky is blue   ")


@print_inp_op
def reverse_sentence_optimized_best(inp: str):
    """
    TC = O(N), SC = O(N)
    :param inp:
    :return:
    """
    return " ".join(reversed(inp.split()))

reverse_sentence_optimized_best("the   sky is blue   ")

from functools import wraps


def print_inp_op(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            print(f"Input args -> {args}")
        if kwargs:
            print(f"Input kwargs -> {kwargs}")
        result = func(*args, **kwargs)
        print(f"{result=}")
        return result

    return wrapper

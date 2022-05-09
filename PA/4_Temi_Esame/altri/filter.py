def my_add(a, b):
    if b == 0:
        return a
    return my_add(a+1, b-1)


def my_mul(a, b):
    if b == 1:
        return a
    return my_add(a, my_mul(a, b-1))


def my_pow(a, b):
    if b == 0:
        return 1
    return my_mul(a, my_pow(a, b-1))


if __name__ == '__main__':
    assert(my_pow(3, 3) == 3 ** 3)
    assert(my_pow(3, 1) == 3 ** 1)
    assert(my_pow(3, 0) == 3 ** 0)
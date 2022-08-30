from es2 import sin, fact

if __name__ == "__main__":
    # for n in range(10):
    #     print("sin({}, {}) => {:.4f}".format(.5, n, sin(.5, n)))

    # print(sin.cache)

    for n in [5, 7, 10, 8, 12, 9]:
        print("fact({}) => {}".format(n, fact(n)))

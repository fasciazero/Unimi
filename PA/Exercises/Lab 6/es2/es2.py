def memoization(f):
    def wrapper(*args):
        print(*args)
        print(f)
        print(wrapper.cache)
        if args not in wrapper.cache:
            wrapper.cache[args] = f(*args)
        else:
            print("### cached value for {} --> {}".format(args, wrapper.cache[args]))
        return wrapper.cache[args]
    
    wrapper.cache = dict()
    return wrapper

@memoization
def fact(n):
    print('ciao')
    return 1 if n <= 1 else n*fact(n-1)

@memoization
def sin(x, n):
    if n == 0: return x
    return (-1**n)/fact(2*n+1)*x**(2*n+1) + sin(x, n-1)

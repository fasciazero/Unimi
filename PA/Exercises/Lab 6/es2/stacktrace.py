def stacktrace(f):
    stacktrace.estack = []
    def wrapper(*args, **kwargs):
        stacktrace.estack = [(f.__name__, args)] + stacktrace.estack
        print("### STACKTRACE")
        print(stacktrace.estack)
        print(*["*** {}{}".format(f[0], f[1]) for f in stacktrace.estack], sep='\n')
        res = f(*args)
        stacktrace.estack = stacktrace.estack[1:]
        return res
    return wrapper

@stacktrace
def fact(n):
    return 1 if n <= 1 else n*fact(n-1)

@stacktrace
def sin(x, n):
    if n == 0: return x
    return (-1**n)/fact(2*n+1)*x**(2*n+1) + sin(x, n-1)

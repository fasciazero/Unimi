def caching(cache, *args, funct):
    if cache == []: return list(args[1:])
    return [funct(cache[j], args[j+1]) for j in range(len(args)-1)]

def multi_triggered(n, cacher):
    def actual_decorator(f):
        def make_decorator(*args):
            make_decorator.count += 1
            make_decorator.stored = caching(make_decorator.stored, *args, funct=cacher)
            if make_decorator.count == n:
                make_decorator.count = 0
                return f(args[0], *make_decorator.stored)
        make_decorator.count = 0
        make_decorator.stored = []
        return make_decorator
    return actual_decorator

def MultiTriggered(rules):
    class Meta(type):
        def __new__(cls, classname, supers, classdict):
            for attr, attrfun in classdict.items():
                if attr in rules.keys():
                    classdict[attr] = multi_triggered(*(rules[attr]))(attrfun)
            return type.__new__(cls, classname, supers, classdict)
    return Meta
